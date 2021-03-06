# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User

from django.conf import settings
from django.template.loader import render_to_string


class Media(models.Model):

    title = models.CharField(max_length=64, verbose_name="Titolo")
    url = models.URLField(unique=True)
    description = models.TextField(default='', blank=True, verbose_name="Descrizione")

    tag_place = models.CharField(
        max_length=64, verbose_name="Territorio", blank=True, default='Fabriano',
        help_text="Territorio di riferimento del contenuto")
    tag_subject = models.CharField(
        max_length=1024, verbose_name="Temi",
        help_text="Temi trattati separati da ',' (virgola)", blank=True, default='')

    dedication = models.TextField(default='', blank=True, verbose_name="Dedica")

    author_name = models.CharField(max_length=64, verbose_name="autore", blank=True)
    author_email = models.EmailField(verbose_name="email", blank=True)
    author_avatar = models.URLField(verbose_name="link all'immagine dell'autore", blank=True)
    author_website = models.URLField(verbose_name="pagina web dell'autore", blank=True)

    approved = models.BooleanField(default=False)
    approved_on = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(User, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    email_to = models.CharField(max_length=1024, blank=True, default='')
    is_private = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/ui/#app/wish/{}'.format(self.pk)

    @property
    def wish_full_url(self):
        if self.url.startswith("http"):
            return self.url
        else:
            if settings.ABS_URL.endswith('/'):
                if self.url.startswith('/'):
                    url = settings.ABS_URL[:-1] + self.url
                else:
                    url = settings.ABS_URL + self.url
            else:
                if self.url.startswith('/'):
                    url = settings.ABS_URL + self.url
                else:
                    url = settings.ABS_URL + '/' + self.url
            return url

    @property
    def is_public(self):
        return not self.is_private

    @property
    def kind(self):
        if self.url.find("img/fabriano") != -1:
            return "wishes_fabriano"
        else:
            return "wishes_other"

    def send_by_email(self):
        if self.email_to:
            abs_fullurl = settings.ABS_URL + self.get_absolute_url()
            txt_msg = u"""
Ciao!

{} ti ha spedito un augurio da Fabriano.

{}

Lo puoi vedere all'indirizzo {}

---
Il messaggio è stato inviato dal progetto FabrianoDigital - http://fabrianodigital.it
            """.format(self.author_name, self.dedication, abs_fullurl)

            recipients = self.email_to.split(',')
            html_msg = render_to_string("digitalxmas/email_msg.html", {
                'obj': self,
                'abs_fullurl': abs_fullurl,
            })
            eml = EmailMultiAlternatives(
                u"[DA FABRIANO] {}".format(self.title),
                txt_msg, self.author_email, bcc=recipients)
            eml.attach_alternative(html_msg, 'text/html')
            eml.send()
            self.email_sent = True
            self.save()

        else:
            raise ValueError("nessun destinatario specificato")

    def save(self, *args, **kw):

        if self.pk:
            old = Media.objects.get(pk=self.pk)
            if old.approved != self.approved:
                if self.approved and not self.approved_on:
                    self.approved_on = timezone.now()
                else:
                    self.approved_on = None

        super(Media, self).save(*args, **kw)

    class Meta:
        verbose_name = "contenuto multimediale"
        verbose_name_plural = "contenuti multimediali"
