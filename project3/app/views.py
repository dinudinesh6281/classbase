from django.shortcuts import render
from  django.views.generic import * 
from app.forms import *

# Create your views here.

from django.http import HttpResponse


def Fun(request):
    return HttpResponse('done with function based view')


class Cfun(View):
    def get(self,request):
        return HttpResponse('done with class based views')


def Htmlfun(request):
    return render(request,'fun2.html')


class CHtmlfun(View):
    def get(self,request):
        return render(request,'fun1.html')


def Stu(request):
    SFO=Studentform()
    d={'SFO':SFO}
   
    if request.method=='POST':
        SFDO=Studentform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Done')
        else:
            return HttpResponse('Invalid')
    return render(request,'stu1.html',d)


class Cstu(View):
    def get(self,request):
        ESFO=Studentform()
        d={'ESFO':ESFO}
        return render(request,'stu2.html',d)
    
    def post(self,request):
        SFDO=Studentform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('DOne')
        else:
            return HttpResponse('Invalid')
    
