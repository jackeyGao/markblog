# -*- coding:utf-8 -*-
from django.db import models
from markdown import markdown

# Create your models here.



class Tag(models.Model):
    name = models.CharField(u'标签名称', max_length=50)
    description = models.TextField(u"标签描述")

    def __unicode__(self):
        return self.name

class BlogTemplate(models.Model):
    name = models.CharField(u'模板名称',max_length=20)
    content = models.TextField(u'模板构造')
    def __unicode__(self):
        return self.name 

class Category(models.Model):
    name = models.CharField(u'类目名称', max_length=20)
    description = models.TextField(u"类目描述")

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title     = models.CharField(u'日志标题',max_length=50)
    slug      = models.CharField(u'日志URL',max_length=45)
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
        return markdown(self.content, ["codehilite"])

    def get_tag_list(self):
        return ','.join([ x.name for x in self.tags.all() ])

    def get_full_content(self):
        if self.is_valid:
            page_full_url = self.get_absolute_url()
            return self.content + "\n\n" + blog_template % page_full_url + "\n\n" + '\n'.join(url_list)
        else:
            return self.content

