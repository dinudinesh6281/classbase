from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from app.models import *

from django.views.generic import *

class Schoolvi(ListView):
    model=School
    context_object_name='school'


class Schooldetv(DetailView):
    model=School
    context_object_name='school'