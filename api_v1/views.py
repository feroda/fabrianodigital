from django.shortcuts import render

from rest_framework import serializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.renderers import JSONRenderer

from digitalxmas.models import Media


class WishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = (
            'id', 'title', 'url', 'description',
            'dedication', 'author_name', 'created_on',
            'author_avatar',
            'tag_place', 'tag_subject', 'kind'
        )


class WishCreateReadView(ListCreateAPIView):

    serializer_class = WishSerializer
    queryset = Media.objects.all()
    renderer_classes = (JSONRenderer, )
