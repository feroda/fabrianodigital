
from django import template

register = template.Library()


@register.simple_tag
def player(media):
    # TODO: preview for other kind of content
    if media.url.find('youtube.com') != -1:
        youtube_id = media.url[media.url.find("?v=")+3:]
        embed_url = "http://www.youtube.com/embed/{}?autoplay=0".format(youtube_id)
        return '<iframe width="420" height="315" src="{}"> </iframe>'.format(embed_url)
    else:
        return '<h3>{media.title}</h3><p>{media.url}'.format(media=media)
