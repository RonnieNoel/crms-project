from django.urls import path
from login.views import LoginView,RegisterView,AuthenticationView,HomeView,LogoutView

urlpatterns=[
    path('',HomeView,name="home"),
    path('login/',LoginView,name="login"),
    path('register/',RegisterView,name="register"),
    path('validation_form',AuthenticationView,name="validation_form"),
    path('logout/',LogoutView,name="logout")
]