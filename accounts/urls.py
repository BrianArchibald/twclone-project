from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    re_path('login/.*', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]