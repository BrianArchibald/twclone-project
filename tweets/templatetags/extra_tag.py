from django import template
from ..models import Message


register = template.Library()


@register.filter(name='messages')
def messages(user):
    message_count = Message.objects.filter(user_to=user, read=False).count()
    if message_count:
        return message_count
    else:
        return ""