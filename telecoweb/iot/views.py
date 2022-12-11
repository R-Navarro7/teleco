from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import  render
from django.urls import reverse
from datetime import datetime as dt
from .models import Meassure
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.
@csrf_exempt
def index(request):
    meassure_list = Meassure.objects.all().values()
    m_len = len(meassure_list)
    plot_list = meassure_list[m_len-30:]
    context = {"meassure_list" : meassure_list, "plot_list": plot_list}
    return render(request, 'iot/test.html', context)

@csrf_exempt
def update(request):
    meassure_list = Meassure.objects.all().values()
    json_response = {}
    json_response['temp_value'] = meassure_list[0]['temp_value']
    json_response['hum_value'] = meassure_list[0]['hum_value']
    json_response['pub_date'] = meassure_list[0]['pub_date']  
    return JsonResponse(json_response)

    
@csrf_exempt
def add_meassure(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
        Meassure.objects.create(temp_value=data['temp'],hum_value=data['hum'],pub_date=dt.now())       
        return HttpResponseRedirect('/')
    else:
        pass
    return HttpResponseRedirect('/')

@csrf_exempt
def main(request):
    return render(request, 'iot/main.html', context = {'label':'Hello World'})

