from django.conf.urls import patterns, include, url

from django.contrib import admin
from values import views as values

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', values.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^values/', include('values.urls')),
)
