from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from templates import web

# Create your views here.

def index(request):
    template = loader.get_template('web/index.html')
    return HttpResponse(template.render())