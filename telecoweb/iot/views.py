from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render
from django.urls import reverse
from django.utils import timezone
from .models import Meassure
# Create your views here.
def index(request):
    meassure_list = Meassure.objects.order_by('-pub_date')[:50]
    context = {meassure_list : "meassure_list"}
    return render(request, 'iot/index.html', context)

def add_meassure(request, temp, hum):
    meassure_db = Meassure()
    meassure_db
    return HttpResponse("200 OK")