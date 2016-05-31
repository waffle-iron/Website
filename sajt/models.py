from django.db import models
from django.conf import settings


class Subscriber(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100, unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    lead = models.TextField(max_length=255, blank=True)
    picture = models.ImageField(upload_to="static", blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField()
    category = models.ForeignKey('Category')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    about = models.TextField(blank=True)
    picture = models.ImageField(blank=True)
    social_twitter = models.CharField(max_length=255, blank=True)
    social_facebook = models.CharField(max_length=255, blank=True)
    social_github = models.CharField(max_length=255, blank=True)
    social_linkedin = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=70)
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True)
    lecturer = models.ForeignKey('Lecturer')

    def __str__(self):
        return self.name
