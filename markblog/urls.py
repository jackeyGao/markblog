# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

admin.site.site_header = 'MarkBlog Management'

urlpatterns = [
    # Examples:
    # url(r'^$', 'markblog.views.home', name='home'),
    url(r'^', include('markbook.urls')),
    #url(r'^grappelli/', include('grappelli.urls')), 
    url(r'^admin/', include(admin.site.urls)),
]
