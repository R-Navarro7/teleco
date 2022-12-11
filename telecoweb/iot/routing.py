from django.urls import path
from .consumers import GraphConsumer

ws_urlpatterns = [
    path('ws/iot/', GraphConsumer.as_asgi())
]