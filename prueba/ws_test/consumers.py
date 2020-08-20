# Channels
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class TestConsumer(JsonWebsocketConsumer):
    """ Create the Seller room, and is the only available to send messages to client"""

    def connect(self):
        self.group_name = "test_room"

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive_json(self, content):
        self.send_json(content)
        # async_to_sync(self.channel_layer.group_send)(
        #     self.group_name, {
        #         'type': 'echo_message',
        #         'product': content
        #     }
        # )
