from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import News
from django.template import RequestContext


def homepage(request):
    return TemplateResponse(request, "homepage.html", {"vesti": News.objects.all()})
