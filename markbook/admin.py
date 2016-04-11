# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from models import *

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name', 'description')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name', 'description')

class BlogTemplateAdmin(admin.ModelAdmin):
    list_display  = ('name','content',)
    search_fields = ('name','content')
    list_display_links = ('name',)


class BlogAdmin(admin.ModelAdmin):
    list_display  = ('title','created', 'template', 'is_reply',
            'is_valid','get_tags', 'category', 'viewpost')
    search_fields = ('title','content')
    list_filter   = ('is_reply','is_valid','updated', 'tags', 'category')
    list_display_links = ('title',)
    ordering = ('-created',)
    date_hierarchy = 'updated' 

    def viewpost(self, obj):
        return '<a href="/post/%s">View</a>' % obj.slug

    def get_tags(self, obj):
        return obj.get_tag_list()

    viewpost.allow_tags = True
    viewpost.short_description = u"查看"

    get_tags.short_description = u"标签"


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogTemplate, BlogTemplateAdmin)
