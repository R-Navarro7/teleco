from django.urls import path

from . import views


app_name = 'iot'
urlpatterns = [
    # ex: /iot/
    path('', views.index, name='index'),
    # ex: /iot/post/"
    path('post/', views.add_meassure, name='add_meassure')
    # ex: /iot/update
    path('update/', views.update, name='update')
]