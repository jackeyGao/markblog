from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'markblog.views.home', name='home'),
    url(r'^', include('markbook.urls')),
    url(r'^grappelli/', include('grappelli.urls')), 
    url(r'^admin/', include(admin.site.urls)),
]
