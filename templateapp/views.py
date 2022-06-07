from os import name
from django.shortcuts import render 
import datetime

# Create your views here.
def display(request):

    return render(request, 'templateapps/html.html')
