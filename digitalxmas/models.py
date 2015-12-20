from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User


class Media(models.Model):

    title = models.CharField(max_length=64, verbose_name="Titolo")
    url = models.URLField(unique=True)
    description = models.TextField(default='', blank=True, verbose_name="Descrizione")

    tag_place = models.CharField(
        max_length=64, verbose_name="Territorio", blank=True, default='Fabriano',
        help_text="Territorio di riferimento del contenuto")
    tag_subject = models.CharField(
        max_length=1024, verbose_name="Temi",
        help_text="Temi trattati separati da ',' (virgola)")

    dedication = models.TextField(default='', blank=True, verbose_name="Dedica")

    author_name = models.CharField(max_length=64, verbose_name="autore", blank=True)
    author_email = models.EmailField(verbose_name="email", blank=True)
    author_avatar = models.URLField(verbose_name="link all'immagine dell'autore", blank=True)
    author_website = models.URLField(verbose_name="pagina web dell'autore", blank=True)

    approved = models.BooleanField(default=False)
    approved_on = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(User, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('media-detail', kwargs={'pk': self.pk})

    @property
    def kind(self):
        if self.url.find("youtube") != -1:
            return "wishes_other"
        else:
            return "wishes_fabriano"

    class Meta:
        verbose_name = "contenuto multimediale"
        verbose_name_plural = "contenuti multimediali"
