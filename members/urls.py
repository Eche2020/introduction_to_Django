from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('myFirst/', views.myFirst, name='myFirst'),
    path('login/', views.login, name='login'),
    path('signIn/', views.signIn, name='signIn'),
]