from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('scimol/',views.index_view, name='index'), 
    path('scimol/BMI/',views.Scimol_BMI_View, name="BMI"),
    path('scimol/vector/',views.Scimol_vector_View, name="vector"),
    path('scimol/coffee/', views.Coffee_View, name='coffee')
       
]