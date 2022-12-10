from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render
from django.urls import reverse
from django.utils import timezone
from .models import Meassure
from django.views.decorators.csrf import csrf_exempt


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
    m_len = len(meassure_list)
    plot_list = meassure_list[m_len-30:]
    context = {"meassure_list" : meassure_list, "plot_list": plot_list}
    return context

@csrf_exempt
def add_meassure(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
        Meassure.objects.create(temp_value=data['temp'],hum_value=data['hum'],pub_date=timezone.now())       
        return HttpResponseRedirect('/')
    else:
        pass
    return HttpResponseRedirect('/')

