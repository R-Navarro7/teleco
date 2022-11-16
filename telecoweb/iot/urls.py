from django.urls import path

from . import views


app_name = 'iot'
urlpatterns = [
    # ex: /iot/
    path('', views.index, name='index'),
    # ex: /temp/"23.5"/hum/"0.67"
    path('temp/<str:temp>/hum/<str:hum>/', views.add_meassure, name='add_meassure')
]