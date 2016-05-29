from django.conf.urls import url
from django.contrib import admin
from sajt import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/([0-9]+)$', views.blog_post, name='blog_post'),
    url(r'^event/$', views.events)
]
