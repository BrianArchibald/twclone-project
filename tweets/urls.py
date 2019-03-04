from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:tweet_id>', views.detail, name='detail'),
    path('add_comment', views.add_comment, name='add_comment')
]