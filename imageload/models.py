from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=20)
    type = models.CommaSeparatedIntegerField(max_length=255, default="1,2",blank=True)
    def __str__(self):
        return self.title.encode('utf-8')




class PropertyImage(models.Model):
    property = models.ForeignKey('Photo',related_name='images')
    image = models.ImageField()

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.image.storage, self.image.path
        # Delete the model before the file
        super(PropertyImage, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

