from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^wishes/$', views.WishCreateReadView.as_view(), name='api-v1-wish-list'),
)
