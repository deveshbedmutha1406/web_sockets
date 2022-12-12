from django.shortcuts import render
from channels.layers import get_channel_layer
from .consumers import *
import time
import json

# Create your views here.

async def index(request):
    # for i in range(1, 10):
    #     channel_layer = get_channel_layer()
    #     data = {'count' : i}
    #     await (channel_layer.group_send)(
    #         'new_consumer_group', {
    #             'type' : 'send_fun',
    #             'value' : json.dumps(data)
    #         }
    #     )
    #     time.sleep(1)
    return render(request, 'index.html')


