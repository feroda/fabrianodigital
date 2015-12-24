
from rest_framework import serializers
from rest_framework import generics
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


class WishCreateReadView(generics.ListCreateAPIView):

    serializer_class = WishSerializer
    queryset = Media.objects.filter(approved=True, is_private=False)
    renderer_classes = (JSONRenderer, )
