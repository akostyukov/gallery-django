from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('<pk>/', views.ImageView.as_view(), name='index'),
    path('<pk>/add-comment', views.SubmitCommentView.as_view(), name='submit'),
]
