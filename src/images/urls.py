from django.urls import path
from . import views

app_name = 'images'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddImageView.as_view(), name='add-image'),
    path('<pk>/like/', views.LikeView.as_view(), name='like'),
    path('<pk>/', views.ImageView.as_view(), name='image'),
    path('<pk>/add-comment/', views.AddCommentView.as_view(), name='add-comment'),
    path('<pk>/get-comments/', views.GetCommentsView.as_view(), name='get-comments'),
]
