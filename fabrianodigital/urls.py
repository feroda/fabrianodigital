from django.conf.urls import patterns, include, url
from django.contrib import admin

from digitalxmas.views import MediaCreate, MediaUpdate, MediaDelete

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fabrianodigital.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'media/add/$', MediaCreate.as_view(), name='media-add'),
    url(r'media/(?P<pk>[0-9]+)/$', MediaUpdate.as_view(), name='media-update'),
    url(r'media/(?P<pk>[0-9]+)/delete/$', MediaDelete.as_view(), name='media-delete'),
)
