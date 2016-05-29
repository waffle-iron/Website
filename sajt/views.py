from django.shortcuts import render
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from .models import News, Event
from django.template import RequestContext


def homepage(request):
    return TemplateResponse(request, "homepage.html", {"vesti": News.objects.all()})


def blog(request):
    return TemplateResponse(request, "blog.html", {"items": News.objects.all()})


def blog_post(request, blog_id):
    blog = get_object_or_404(News, pk=blog_id)
    return TemplateResponse(request, "blog_post.html", {"item": blog})


def events(request):
    return TemplateResponse(request, "events.html", {"items": Event.objects.all()})
