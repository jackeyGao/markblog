# -*- coding:utf-8 -*-
import misaka as m
from django.db import models
from renderer import BleepRenderer

# Create your models here.

# markdown bleeprenderer instance
renderer = BleepRenderer()
mdown = m.Markdown(renderer,
    extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS)

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
    is_reply  = models.BooleanField(u'是否评论')
    is_valid  = models.BooleanField(u'是否有效')
    created   = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated   = models.DateTimeField(u'更新时间', auto_now=True)

    def __unicode__(self):
        return self.title

    def context_markup(self):
        full_content = self.get_full_content()
        return mdown.render(full_content)

    def get_tag_list(self):
        return ','.join([ x.name for x in self.tags.all() ])

    def get_context(self):
        return { 
            "BLOG_CONTENT": self.content ,
            }

    def get_full_content(self):
        context = self.get_context()
        full_content = self.template.content.format(**context)
        return full_content

