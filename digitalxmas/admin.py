from django.contrib import admin

from digitalxmas.models import Media


class MediaAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'author_name', 'approved')
    actions = ['approve']

    def approve(self, request, queryset):

        for obj in queryset:
            obj.approved = True
            obj.save()

    approve.short_description("Approva messaggi")


admin.site.register(Media, MediaAdmin)
