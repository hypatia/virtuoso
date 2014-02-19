from django.conf.urls import patterns, url

from values import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /values/5/
    url(r'^(?P<value_id>\d+)/$', views.detail, name='detail'),
)