from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import View
class first(View): #class based view
     def get(self,request):
        return HttpResponse("good luck")


# Create your views here.
