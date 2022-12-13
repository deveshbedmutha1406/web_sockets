from django.shortcuts import render
from channels.layers import get_channel_layer
from django.http import JsonResponse
from .consumers import *
from .thread import *
import time
import json

# Create your views here.

async def index(request):
    return render(request, 'index.html')


def generate_student_data(request):
    total = request.GET.get('total')
    CreateStudentsThread(int(total)).start()
    return JsonResponse({"status" : 200})
