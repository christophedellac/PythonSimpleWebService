from django.conf.urls import patterns, url

from FlickrDjango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<to_search>[\w ]+)/$', views.detail, name='detail'),
)
