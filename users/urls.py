from kongoni_web import urls
from django.urls import path
from django.contrib.auth import login
from .import views

app_name = 'users'
urlpatterns = [
    # register
    path("register/", views.register_request, name="register"),
    # login page
    path('login/', views.login_request, name="login"),
    # Logout page
    path('logout/', views.logoutUser, name='logout'),
]