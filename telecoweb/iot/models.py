from django.db import models

# Create your models here.
class Meassure(models.Model):
    temp_value = models.CharField(max_length=200)
    hum_value = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    