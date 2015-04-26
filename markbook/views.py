# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.conf import settings

from models import *


class BaseMixin(object):
    def get_context_data(self, *args, **kwargs):
        if 'object' in kwargs or 'item_name' in kwargs:
            context = super(BaseMixin, self).get_context_data(**kwargs)
        else:
            context = {}

        try:
            context['blog_name'] = settings.CUSTOM_BLOG_NAME
            context['author'] = settings.CUSTOM_BLOG_AUTHOR
            context['description'] = settings.CUSTOM_BLOG_DESCRIPTION
        except Exception as e:
            logger.exception(u'加载基本信息出错[%s]！', e)
        return context


class IndexListView(BaseMixin, ListView):
    queryset = Blog.objects.filter(is_valid=1).order_by("-updated")[:6]
    context_object_name = 'posts'
    template_name = "markbook/index.html"


    def get_context_data(self, **kwargs):
        kwargs["object"] = None
        return super(IndexListView, self).get_context_data(**kwargs)


class PostDetailView(BaseMixin, DetailView):
    model = Blog
    template_name = "markbook/post.html"
    slug_field = "slug"
    context_object_name = "post"

class PostListView(BaseMixin, ListView):
    model = Blog
    context_object_name = 'posts'
    template_name = "markbook/list.html"

    def get_context_data(self, **kwargs):
        kwargs['item_name'] = self.kwargs.get('item_name')
        return super(PostListView, self).get_context_data(**kwargs)

class TagPostListView(PostListView):

    def get_queryset(self):
        self.name = self.kwargs.get('item_name')
        tags = Tag.objects.filter(name=self.name)
        queryset = Blog.objects.filter(tags__in=tags, 
                is_valid=1).order_by("-updated")
        return queryset

class CategoryPostListView(PostListView):

    def get_queryset(self):
        self.name = self.kwargs.get('item_name')
        categorys = Category.objects.filter(name=self.name)
        queryset = Blog.objects.filter(category__in=categorys, 
                is_valid=1).order_by("-updated")
        return queryset

class TagsListView(BaseMixin, ListView):
    context_object_name = 'tags'
    template_name = "markbook/tags.html"

    def get_queryset(self, **kwargs):
        posts = Blog.objects.all()
        tags  = Tag.objects.all()
        queryset = []
        for tag in tags:
            post_number = [ post for post in posts if tag in post.tags.all() ]
            tag.number = len(post_number)
            queryset.append(tag)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs["object"] = None
        return super(TagsListView, self).get_context_data(**kwargs)

class ArchivesListView(BaseMixin, ListView):
    context_object_name = "archives"
    template_name = "markbook/archives.html"

    def get_queryset(self, **kwargs):
        queryset = {}
        for post in Blog.objects.all():
            year = post.created.year
            if not queryset.has_key(year):
                queryset[year] = [post,]
            else:
                year_list = queryset[year]
                year_list.append(post)
                queryset[year] = year_list
        
        for year in queryset:
            year_list = queryset[year]
            year_list = sorted(year_list, key = lambda asd:asd.created, reverse = True)
            queryset[year] = year_list

        queryset = sorted(queryset.iteritems(), key = lambda asd:asd[0], reverse = True)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs["posts"]  = Blog.objects.all()
        kwargs["object"] = None
        return super(ArchivesListView, self).get_context_data(**kwargs)
