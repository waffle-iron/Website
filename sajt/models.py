from django.db import models
from django.conf import settings


class Subscriber(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    picture = models.ImageField(upload_to="static", blank=True)
    publish_date = models.DateField()
    create_date = models.DateField()
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
    description = models.TextField()
    create_date = models.DateField()
    picture = models.ImageField()
    lecturer = models.ForeignKey('Lecturer')

    def __str__(self):
        return self.name
