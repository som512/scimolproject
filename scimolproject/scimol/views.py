from urllib import request
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import mol



def index_view(request):
    object_list = mol.objects.order_by('-id')

    return render(request, 'scimol/index.html', {'object_list': object_list})
    

def Scimol_BMI_View(request):
    object_list = mol.objects.order_by('-id')
    return render(request, 'scimol/scimol_BMI.html', {'object_list': object_list})

def Scimol_vector_View(request):
    object_list = mol.objects.order_by('-id')
    return render(request, 'scimol/scimol_vector.html', {'object_list': object_list})

def Coffee_View(request):
    return render(request, 'scimol/coffee.html')
