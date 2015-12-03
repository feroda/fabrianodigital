from django.db import models

from django.contrib.auth.models import User


class Media(models.Model):

    title = models.CharField(max_length=64)
    url = models.URLField()
    description = models.TextField(default='', blank=True)

    tag_place = models.CharField(
        max_length=64, verbose_name="Territorio", blank=True,
        help_text="Inserire il territorio di riferimento del contenuto")
    tag_subject = models.CharField(
        max_length=1024, verbose_name="Temi",
        help_text="Inserire i temi trattati separati da ',' (virgola)")

    author = models.CharField(max_length=64)
    author_logo = models.ImageField()

    approved = models.BooleanField(default=False)
    approved_on = models.DateTimeField(null=True)
    approved_by = models.ForeignKey(User, null=True)


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('media-detail', kwargs={'pk': self.pk})
    class Meta:
        verbose_name = "contenuto multimediale"
        verbose_name_plural = "contenuti multimediali"
