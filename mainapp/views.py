from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
import json
# Create your views here.
from django.template import RequestContext
def home(request):
    return render(request, 'mainapp/index.html', {
        'room_name': "broadcast"
    })

from asgiref.sync import async_to_sync
def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': json.dumps("Notification")
        }
    )
    return HttpResponse("Done")