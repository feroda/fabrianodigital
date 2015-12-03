from django.contrib import admin

from digitalxmas.models import Media


class MediaAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'author')

admin.site.register(Media, MediaAdmin)
