from django.db import models

# Create your models here.
class Meassure(models.Model):
    temp_value = models.CharField(max_length=200)
    hum_value = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return str([self.temp_value, self.hum_value, self.pub_date])