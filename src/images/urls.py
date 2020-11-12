from django.urls import path, include
from . import views

app_name = 'images'
urlpatterns = [
    path('', views.ImageView.as_view(), name='index'),
    path('add/', views.AddImage.as_view(), name='add_image'),
]
