from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from sensor_management.consumer import AlertConsumer


application = ProtocolTypeRouter({
    # Empty
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    # SALESMAN MAP ROOM
                    re_path(r"^salesman_map_room/(?P<alert_id>)", AlertConsumer.as_asgi()),

                ]
            )
        )
    )
})
