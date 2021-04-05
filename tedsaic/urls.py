from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addImage', views.add_image, name='addImage'),
]