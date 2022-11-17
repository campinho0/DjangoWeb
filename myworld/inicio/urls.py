from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register/adduser/', views.add, name='add'),
    path('register/adduser/newuser/', views.addUsuario, name='addUsuario'),
]