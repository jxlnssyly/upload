from django.conf.urls import include, url
import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^photography',views.photography),
    url(r'^design',views.design),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)