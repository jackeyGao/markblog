from django.contrib import admin

#coding=UTF-8
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
    list_display  = ('title','created','updated', 'template', 'is_reply',
            'is_valid','get_tag_list', 'slug')
    search_fields = ('title','content')
    list_filter   = ('is_reply','is_valid','updated')
    list_display_links = ('title',)
    ordering = ('-created',)
    date_hierarchy = 'updated' 



# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogTemplate, BlogTemplateAdmin)
