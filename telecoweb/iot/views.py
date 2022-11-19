from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render
from django.urls import reverse
from django.utils import timezone
from .models import Meassure
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    meassure_list = Meassure.objects.all().values()
    context = {"meassure_list" : meassure_list}
    return render(request, 'iot/index.html', context)

@csrf_exempt
def add_meassure(request):
    if request.method == 'POST':
        data = request.POST.dict()
        Meassure.objects.create(temp_value=data['temp'],hum_value=data['hum'],pub_date=timezone.now())        
        return HttpResponseRedirect('/')
    else:
        pass
    return HttpResponseRedirect('/')