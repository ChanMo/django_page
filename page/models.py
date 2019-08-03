from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

class Page(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
            blank=True, null=True)
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), max_length=200, unique=True)
    content = RichTextField(_('content'), blank=True, null=True)
    is_active = models.BooleanField(_('is active'), default=True)
    template = models.CharField(_('template'), default='detail',
            max_length=100)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/page/%s/' % self.slug

    class Meta:
        ordering = ['-created']
        verbose_name = _('page')
        verbose_name_plural = _('page')
