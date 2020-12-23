from django.urls import path
from . import views

app_name = 'authorization'

urlpatterns = [
    path('login/', views.Login.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
