from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:tweet_id>', views.detail, name='view'),
    path('add_comment/<int:tweet_id>', views.add_comment, name='add_comment'),
]