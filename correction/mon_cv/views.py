from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.template import loader


def index(request):
    template = loader.get_template('mon_cv/index.html')
    a = Skills.objects.all()
    context = {
        "a" : a
    }
    print(a)
    return HttpResponse(template.render(context, request))