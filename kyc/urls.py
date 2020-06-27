from django.urls import path, include
from . import views

urlpatterns = [
path('upload_xml/', views.upload_xml, name="upload_xml"),
path('<customer_id>/', views.confirm, name = 'confirm'),
]