from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:tweet_id>', views.detail, name='view'),
    path('add_comment/<int:tweet_id>', views.add_comment, name='add_comment'),
    path('edit/<int:tweet_id>', views.edit_post, name='edit_post'),
    path('delete/<tweet_id>', views.delete, name='delete'),
    path('messages', views.messages, name='message'),

]