from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async


class AlertConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.alert_id = None
        self.thread_name = None

    async def websocket_connect(self, event):
        self.alert_id = self.scope['path_remaining']
        self.thread_name = f"alert_request_{self.alert_id}"
        await self.channel_layer.group_add(
            self.thread_name,
            self.channel_name
        )
        await self.accept()

    async def websocket_receive(self, event):
        await self.channel_layer.group_send(
            self.thread_name,
            {
                "type": "send.message",
                "data": event['text']
            }
        )

    async def send_message(self, event):
        await self.send_json(event['data'])

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(
            self.thread_name,
            self.channel_name
        )
        await self.disconnect(event['code'])
        raise StopConsumer()

    @database_sync_to_async
    def fetch_device_data(self):
        pass