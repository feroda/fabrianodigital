from django.conf.urls import patterns, include, url
from django.contrib import admin

from base import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'digitalxmas/', include('digitalxmas.urls')),
    url(r'api/v1/', include('api_v1.urls')),
)
