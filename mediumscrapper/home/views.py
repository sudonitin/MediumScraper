from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    # template = loader.get_template('home/index.html')
    return render(request, 'home/index.html')