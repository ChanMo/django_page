#!/usr/bin/python
# vim: set fileencoding=utf8 :
from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    image = models.ImageField(upload_to='page/%Y/%m/%d/', verbose_name='图片', blank=True, null=True)
    intro = models.TextField(verbose_name='描述')
    content = RichTextField(config_name='awesome_ckeditor', verbose_name='内容', blank=True, null=True)
    is_publish = models.BooleanField(default=True, verbose_name='是否发布')
    template = models.CharField(default='default', verbose_name='模板')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    def __unicode__(self):
        return self.title
    class Meta(object):
        verbose_name = '文章'
        verbose_name_plural = '文章'
