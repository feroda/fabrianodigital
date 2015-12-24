# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib import messages

from digitalxmas.models import Media


class MediaAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'author_name',
        'approved', 'email_sent', 'is_private')

    actions = ['approve', 'send_by_email', 'reset_email_sent']

    def approve(self, request, queryset):

        for obj in queryset:
            obj.approved = True
            obj.save()
    approve.short_description = "Approva auguri"

    def send_by_email(self, request, queryset):

        for obj in queryset:
            if obj.email_to:
                if not obj.email_sent:
                    obj.send_by_email()
                else:
                    messages.info(request, u"Email già inviata per {}".format(obj))
            else:
                messages.info(request, u"Destinatari non impostati per {}".format(obj))
    send_by_email.short_description = "Invia gli auguri via email"

    def reset_email_sent(self, request, queryset):

        for obj in queryset:
            obj.email_sent = False
            obj.save()
    reset_email_sent.short_description = "Azzera l'invio email"

admin.site.register(Media, MediaAdmin)
