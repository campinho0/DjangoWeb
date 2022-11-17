from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/logincheck/', views.logincheck, name='logincheck'),
    path('register/', views.register, name='register'),
    path('register/adduser/', views.add, name='add'),
    path('register/adduser/newuser/', views.addUsuario, name='addUsuario'),
    path('register/delete/<int:id>', views.deleteUsuario, name='deleteUsuario'),
]