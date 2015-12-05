from django.conf.urls import patterns, url

from digitalxmas.views import MediaCreate, MediaUpdate, MediaDelete, MediaList

urlpatterns = patterns(
    '',
    url(r'media/$', MediaList.as_view(), name='media'),
    url(r'media/add/$', MediaCreate.as_view(), name='media-add'),
    url(r'media/(?P<pk>[0-9]+)/$', MediaUpdate.as_view(), name='media-update'),
    url(r'media/(?P<pk>[0-9]+)/delete/$', MediaDelete.as_view(), name='media-delete')
)
