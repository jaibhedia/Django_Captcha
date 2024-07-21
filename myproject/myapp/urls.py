from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('users/', views.user_list_view, name='user_list'),
]
