from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PageConfig(AppConfig):
    name = 'page'
    verbose_name = _('page')
