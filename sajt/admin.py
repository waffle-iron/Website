from django.contrib import admin
from .models import News, Category, Event, Lecturer, Subscriber

models = [News, Category, Event, Lecturer, Subscriber]
admin.site.register(models)
