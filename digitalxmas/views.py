from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from digitalxmas.models import Media


class MediaCreate(CreateView):
    model = Media
    fields = ['url', 'title', 'tag_place', 'tag_subject', 'description', 'author', 'author_logo']

    def form_valid(request):
        super(MediaCreate, super).form_valid(request)
        return redirect('media-list')


class MediaList(ListView):
    model = Media


class MediaUpdate(UpdateView):
    pass


class MediaDelete(DeleteView):
    pass
