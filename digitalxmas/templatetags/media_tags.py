from django import template

register = template.Library()

@register.simple_tag
def player(media):
    # TODO: preview for other kind of content
    #Youtube video
    if media.url.find('youtube.com') != -1:
        youtube_id = media.url[media.url.find("?v=")+3:]
        embed_url = "http://www.youtube.com/embed/{}?autoplay=0".format(youtube_id)
        return '<iframe src="{}" class="media-thumbnail"> </iframe>'.format(embed_url)

    #Facebook Video
    elif media.url.find('facebook.com') != -1 and media.url.find('videos/') != -1:
        facebook_id = media.url[media.url.find("videos/")+7:]
        embed_url = "https://www.facebook.com/video/embed?video_id={}".format(facebook_id)
        return '<iframe src="{}" class="media-thumbnail"> </iframe>'.format(embed_url)

    #Generic JPG
    elif media.url.find('.jpg') != -1:
        return '<img src="{}" alt="{}" class="media-thumbnail">'.format(media.url, media.title)

    #Generic GIF
    elif media.url.find('.gif') != -1:
        return '<img src="{}" alt="{}" class="media-thumbnail">'.format(media.url, media.title)

    else:
        return '<h3>{media.title}</h3><p>{media.url}'.format(media=media)
