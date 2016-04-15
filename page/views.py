from django.shortcuts import render
from django.views.generic import DetailView
from .models import Page

class PageView(DetailView):
    model = Page
    def get_template_names(self, **kwargs):
        return 'page/%s.html' % self.object.template
