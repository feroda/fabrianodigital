from django.contrib import admin

from digitalxmas.models import Media


class MediaAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'author_name')

admin.site.register(Media, MediaAdmin)
