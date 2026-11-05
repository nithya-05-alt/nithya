from django.shortcuts import render
from django.http import HttpResponse 
from cse.models import students
from cse.forms import StudentsForm
from django.contrib.auth.decorators import login_required 
@login_required
def cseapp(request):
    a={'name':'nithya','role':'student'}
    return render(request,"cse/index.html",a)
    
def dataView(request):
    k=students.objects.all()
    l={"result":k} #table
    return render(request,'cse/index.html',l)

def adddata(request):  #to add data
    form=StudentsForm #forms.py lo studentsform name
    ModelForm={'form':form} 
    if request.method=='POST':
        form=StudentsForm(request.POST)
        if form.is_valid():
            form.save()
        return dataView(request)
    return render(request,'cse/add_students.html',ModelForm)

def updateData(request,id): #edit the form
    dev=students.objects.get(id=id) 
    va=StudentsForm(instance=dev)
    upd={'form':va}
    if request.method=='POST':
        he=StudentsForm(request.POST,instance=dev)
        if he.is_valid():
            he.save()
        return dataView(request)
    return render(request,'cse/update.html',upd)

def deleteData(request,id):
    fun=students.objects.get(id=id) #to delete
    fun.delete()
    return dataView(request)


