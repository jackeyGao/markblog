# -*- coding:utf-8 -*-
import misaka as m
from django.template import Template
from django.template import Context
from django.utils.encoding import force_text
from django.db import models
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
    name = models.CharField(u'标签名称', max_length=50, unique=True)
    description = models.TextField(u"标签描述")

    def __unicode__(self):
        return self.name

class BlogTemplate(models.Model):
    name = models.CharField(u'模板名称',max_length=20, unique=True)
    content = models.TextField(u'模板构造')
    def __unicode__(self):
        return self.name 

class Category(models.Model):
    name = models.CharField(u'类目名称', max_length=20, unique=True)
    description = models.TextField(u"类目描述")

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title     = models.CharField(u'日志标题',max_length=50, unique=True)
    slug      = models.CharField(u'日志URL',max_length=45, unique=True)
    category  = models.ForeignKey(Category)
    tags      = models.ManyToManyField(Tag)
    template  = models.ForeignKey(BlogTemplate)
    content   = models.TextField(u'日志内容')
    is_reply  = models.BooleanField(u'是否评论', default=True)
    is_valid  = models.BooleanField(u'是否有效', default=True)
    created   = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated   = models.DateTimeField(u'更新时间', auto_now=True)

    def __unicode__(self):
        return self.title

    def context_markup(self):
        full_content = self.get_full_content()
        full_content = force_text(full_content, strings_only=True)
        
        return mdown.render(full_content)

    def get_tag_list(self):
        return ','.join([ x.name for x in self.tags.all() ])

    def get_context(self):
        return Context({"post": self}, autoescape=False)

    def get_full_content(self):
        context = self.get_context()
        template = Template(self.template.content)
        full_content = template.render(context)
        return full_content.__str__()

