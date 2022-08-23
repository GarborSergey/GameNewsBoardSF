from django.urls import path
from . import views

app_name = 'NewsBoard'

urlpatterns = [
    path('test/', views.Testing.as_view(), name='test-page'),
]
