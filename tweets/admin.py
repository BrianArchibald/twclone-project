from django.contrib import admin
from .models import Comment, Tweet, Message

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(Message)
