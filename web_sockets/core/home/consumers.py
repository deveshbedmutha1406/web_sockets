from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json


class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = "testConsumer"
        self.room_group_name = "testConsumerGroup"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({"status": "connected from django channel"}))  # backend to frontend,
        # send it in string form use json.dumps.

    def receive(self, text_data):
        # front end to backend
        print(text_data)
        self.send(text_data=json.dumps(text_data))

    def disconnect(self, *args, **kwargs):
        print("Disconnected")

    def send_fun(self, event):
        var = json.loads(event.get('value'))    # convert to json.
        self.send(text_data=json.dumps({'payload' : var}))  # send in string form use json.dumps.


class NewConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = "new_consumer"
        self.room_group_name = "new_consumer_group"
        await (self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({"status" : "connected from async"}))

    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps(text_data))

    async def disconnect(self, *args, **kwargs):
        print("Disconnected")

    async def send_fun1(self, event):
        var = json.loads(event.get('value'))  # convert to json.
        await self.send(text_data=json.dumps({'payload': var}))  # send in string form use json.dumps.

