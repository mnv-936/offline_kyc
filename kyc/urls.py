from django.urls import path, include
from . import views

urlpatterns = [
path('', views.home, name = 'home'),
path('upload_xml', views.upload_xml, name="upload_xml"),
path('confirm', views.confirm, name = 'confirm'),
]