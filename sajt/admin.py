from django.contrib import admin
from .models import News, Category, Event, Lecturer

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Lecturer)
