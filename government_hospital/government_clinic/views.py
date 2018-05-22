from django.shortcuts import render

# Create your views here.
from django .http import HttpResponse
#from django .shortcuts import get_object_or_404
#from rest_framework .views import APIView
#from rest_framework .response import Response
#from rest_framework import status
from .models import Patients
#from .seriligers import Patientserializer
from django import forms
from django.http import request,HttpResponse

'''class Patients_list(APIView):


    def get(self,request):
        patient1 = Patients.objects.all()
        serializer = Patientserializer(patient1,many= True)
        return Response(serializer.data)

    def post(self):
        pass'''

def home(request):
    return render(request,"home.html")

def list_patient(request):
    data = Patients.objects.all()
    return render(request,"patient.html",{'data':data})



