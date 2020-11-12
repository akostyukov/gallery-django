from django.urls import path
from . import views

app_name = 'authorization'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('create-user/', views.CreateUser.as_view(), name='create-user'),
]
