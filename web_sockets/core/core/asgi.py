"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from home.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


ws_patterns = [
    path("ws/test/", TestConsumer.as_asgi()),
    path("ws/new/", NewConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns),
})