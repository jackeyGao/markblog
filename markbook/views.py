# -*- coding:utf-8 -*-
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from models import Blog, Tag, Category
from function import is_mobile

class BaseMixin(object):
    def get_context_data(self, *args, **kwargs):
        if 'object' in kwargs or 'item' in kwargs:
            context = super(BaseMixin, self).get_context_data(**kwargs)
        else:
            context = {}
        try:
            context['is_mobile'] = is_mobile(self.request.META["HTTP_USER_AGENT"])
            context['blog_name'] = settings.CUSTOM_BLOG_NAME
            context['author'] = settings.CUSTOM_BLOG_AUTHOR
            context['description'] = settings.CUSTOM_BLOG_DESCRIPTION
        except Exception as e:
            pass
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

    def get_queryset(self):
        self.name = self.kwargs.get('item_name')
        item = self.item_class.objects.filter(name=self.name)
        filter_dict = {}
        filter_dict[self.filter_field] = item
        filter_dict['is_valid'] = 1
        queryset = Blog.objects.filter(**filter_dict).order_by("-updated")
        return queryset

    def get_context_data(self, **kwargs):
        item_name = self.kwargs.get("item_name")
        item_obj = self.item_class.objects.get(name=item_name)
        kwargs['item'] = item_obj
        return super(PostListView, self).get_context_data(**kwargs)


class TagPostListView(PostListView):
    item_class = Tag
    filter_field = "tags__in"

class CategoryPostListView(PostListView):
    item_class = Category
    filter_field = "category__in"

class TagsListView(BaseMixin, ListView):
    context_object_name = 'tags'
    template_name = "markbook/tags.html"

    def get_queryset(self, **kwargs):
        posts = Blog.objects.filter(is_valid=1)
        tags  = Tag.objects.all()
        queryset = []
        for tag in tags:
            post_number = [ post for post in posts if tag in post.tags.all() ]
            tag.number = len(post_number)
            queryset.append(tag)

        queryset = sorted(queryset, key = lambda asd:asd.number, reverse = True)

        return queryset

    def get_context_data(self, **kwargs):
        kwargs["object"] = None
        return super(TagsListView, self).get_context_data(**kwargs)

class ArchivesListView(BaseMixin, ListView):
    context_object_name = "archives"
    template_name = "markbook/archives.html"

    def get_queryset(self, **kwargs):
        queryset = {}
        for post in Blog.objects.filter(is_valid=1):
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
        kwargs["posts"]  = Blog.objects.filter(is_valid=1)
        kwargs["object"] = None
        return super(ArchivesListView, self).get_context_data(**kwargs)

def BlogMarkDownSrcView(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return HttpResponse(post.get_full_content().encode('GB18030'), 
            content_type='text/plain')

def error404(request):
    return render_to_response('404.html', { 'page' : ''})
