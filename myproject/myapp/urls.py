from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('my-form/', views.my_view, name='my_form'),
]
