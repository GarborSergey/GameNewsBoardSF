from django.urls import path
from . import views

app_name = 'NewsBoard'

urlpatterns = [
    path('', views.MainPage.as_view(), name='main-page'),

    # =============================== CRUD Post MODEL ===================================
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('post-create/', views.PostCreate.as_view(), name='post-create'),
    path('post-delete/<int:pk>', views.PostDelete.as_view(), name='post-delete'),
    path('post-edit/<int:pk>', views.PostUpdate.as_view(), name='post-edit')
    # ====================================================================================
]
