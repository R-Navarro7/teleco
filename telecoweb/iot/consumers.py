import json
from time import sleep
import random
from channels.generic.websocket import WebsocketConsumer
from django.core import serializers
from asgiref.sync import sync_to_async

class GraphConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while True:
            from .models import Meassure
            meassure_list = Meassure.objects.all().values()
            m_len = len(meassure_list)
            plot_list = meassure_list[m_len-30:]
            response = []
            for i in plot_list:
                json_ = {}
                json_['temp_value'] = i['temp_value']
                json_['hum_value'] = i['hum_value']
                json_['pub_date'] = i['pub_date'].strftime('%d-%m-%Y %H:%M:%S')
                response += [json_]
            self.send(json.dumps(response))
            sleep(1)
