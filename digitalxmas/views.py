from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from digitalxmas.models import Media


class MediaCreate(CreateView):
    model = Media


class MediaUpdate(UpdateView):
    pass


class MediaDelete(DeleteView):
    pass
