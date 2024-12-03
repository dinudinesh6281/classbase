from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.http import *

# Create your views here.

class RenderHtml(TemplateView):
    template_name='fun1.html'
    def get_context_data(self, **kwargs):
        EmptyObj= super().get_context_data(**kwargs)
        EmptyObj['name']='Amin'
        return EmptyObj
    


class StudentInsert(TemplateView):
    template_name='fun.html'
    def get_context_data(self, **kwargs):
        EmptyObj= super().get_context_data(**kwargs)
        EmptyObj['form']=Studentform()
        return EmptyObj
    
    def post(self,request):
        data=Studentform(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("OK")
        else:
           return HttpResponse('NOT OK')