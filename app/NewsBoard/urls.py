from django.urls import path
from . import views

app_name = 'NewsBoard'

urlpatterns = [
    path('', views.MainPage.as_view(), name='main-page'),

    # =============================== CRUD Post MODEL ===================================
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('post-create/', views.PostCreate.as_view(), name='post-create'),
    path('post-delete/<int:pk>/', views.PostDelete.as_view(), name='post-delete'),
    path('post-edit/<int:pk>/', views.PostUpdate.as_view(), name='post-edit'),
    # ====================================================================================

    # My posts
    path('posts/my-posts/', views.all_my_posts, name='my-posts'),

    # Like-Dislike POST (add, remove to(from) favorites)
    path('post/like/<int:pk>/', views.add_post_to_favorites, name='post-like'),
    path('post/dislike/<int:pk>/', views.remove_post_from_favorites, name='post-dislike'),

    # Messages functional
    path('post/<int:pk>/send-message/', views.message_to_post, name='message-to-post'),
    path('post/<int:pk>/messages/', views.message_list_on_post, name='message-list'),
    path('message-remove/<int:pk>/', views.message_delete, name='message-delete'),
    path('message-public/<int:pk>/', views.message_to_publish, name='message-public')  # public(republic)

]
