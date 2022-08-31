from django.urls import path
from . import views

app_name = 'NewsBoard'

urlpatterns = [
    path('', views.MainPage.as_view(), name='main-page'),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('post-create/', views.PostCreate.as_view(), name='post-create'),
]
