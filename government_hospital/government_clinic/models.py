from django.db import models

# Create your models here.

class Patients(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    age = models.CharField(max_length= 5)
    disease = models.CharField(max_length= 50,default= "fever")
    password = models.CharField(max_length=6,default="")
    location = models.CharField(max_length=200,default="hydrabad")


    def __str__(self):
        return self.first_name