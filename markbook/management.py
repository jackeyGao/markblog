# -*- coding: utf-8 -*-
'''
File Name: markbook/management.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: Sun May  3 11:30:21 2015
'''

from django.dispatch import dispatcher
from django.db.models.signals import post_syncdb
from markbook import models as blog_app
from markbook.models import *

def setup_blog(sender, **kwargs):
    BlogTemplate(name="空的模板", content="{{post.content}}").save()
    BlogTemplate(name="博客模板", content="""* **博客标题:** {{post.title}} 
* **博客链接:** [地址](./{{post.slug}})
* **创建时候:** {{post.created}}
* **最后更新:** {{post.updated}}

{{post.content}}""").save()
    Tag(name="sys", description="系统保留").save()
    Category(name="系统页面", description="系统页面").save()

    tag = Tag.objects.get(name="sys")
    template = BlogTemplate.objects.get(name="空的模板")
    b_template = BlogTemplate.objects.get(name="博客模板")
    category = Category.objects.get(name="系统页面")

    links = Blog(title="一些链接", slug="links", category=category, 
        template=template, content="一些链接", is_reply=False, is_valid=False)
    links.save()
    
    about_me = Blog(title="关于我", slug="about-me", category=category, 
        template=template, content="关于我", is_reply=False, is_valid=False)
    about_me.save()

    about_blog = Blog(title="关于博客", slug="about-blog", category=category, 
        template=template, content="关于博客", is_reply=False, is_valid=False)
    about_blog.save()

    helloworld = Blog(title="Hello world", slug="helloworld", category=category, 
        template=b_template, content="这是第一篇博客", is_reply=True, is_valid=True)
    helloworld.save()

    links.tags.add(tag)
    about_me.tags.add(tag)
    about_blog.tags.add(tag)
    links.save()
    about_me.save()
    about_blog.save()


post_syncdb.connect(setup_blog, sender=blog_app)
