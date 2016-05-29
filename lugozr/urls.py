from django.conf.urls import url
from django.contrib import admin
from sajt import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage)
]
