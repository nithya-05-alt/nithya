from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import View
def eceapp(request):
    return HttpResponse("second app eceapp")
class first(View): #class based view
     def get(self,request):
        return HttpResponse("good luck")

