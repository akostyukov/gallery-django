from django.urls import path, include
from . import views

app_name = 'authorization'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register-user/', views.CreateUser.as_view(), name='register-user'),
]
