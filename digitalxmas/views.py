from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from digitalxmas.models import Media


class MediaCreate(CreateView):
    model = Media
    fields = ['url', 'title', 'tag_place', 'tag_subject', 'description', 'author', 'author_logo']


class MediaUpdate(UpdateView):
    pass


class MediaDelete(DeleteView):
    pass