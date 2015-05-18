# -*- coding:utf-8 -*-
import misaka as m
from django.template import Template
from django.template import Context
from django.db import models
from django.contrib.sites.models import Site
from renderer import BleepRenderer

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.

# markdown bleeprenderer instance
renderer = BleepRenderer()
mdown = m.Markdown(renderer,
    extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS |\
            m.EXT_TABLES)

class Tag(models.Model):
    name = models.CharField(u'name', max_length=50, unique=True, primary_key=True)
    description = models.TextField(u"description")

    def __unicode__(self):
        return self.name

class BlogTemplate(models.Model):
    name = models.CharField(u'name',max_length=20, unique=True, primary_key=True)
    content = models.TextField(u'content')
    def __unicode__(self):
        return self.name 

class Category(models.Model):
    name = models.CharField(u'name', max_length=20, unique=True, primary_key=True)
    description = models.TextField(u"description")

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title     = models.CharField(u'Title',max_length=50, unique=True)
    slug      = models.CharField(u'Slug',max_length=45, unique=True)
    category  = models.ForeignKey(Category)
    tags      = models.ManyToManyField(Tag)
    template  = models.ForeignKey(BlogTemplate)
    content   = models.TextField(u'Content')
    is_reply  = models.BooleanField(u'Is_reply', default=True)
    is_valid  = models.BooleanField(u'Is_valid', default=True)
    created   = models.DateTimeField(u'Created', auto_now_add=True)
    updated   = models.DateTimeField(u'Updated', auto_now=True)

    def __unicode__(self):
        return self.title

    def context_markup(self):
        full_content = self.get_full_content()
        return mdown.render(full_content)

    def get_absolute_url(self):
        return 'post/' + self.slug

    def get_full_url(self):
        return 'http://%s/%s' % (Site.objects.get_current().domain, 
                self.get_absolute_url())

    def get_tag_list(self):
        return ','.join([ x.name for x in self.tags.all() ])

    def get_context(self):
        return Context({"post": self}, autoescape=False)

    def get_full_content(self):
        context = self.get_context()
        template = Template(self.template.content)
        full_content = template.render(context)
        return full_content.__str__()

