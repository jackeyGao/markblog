from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'markblog.views.home', name='home'),
    url(r'^blog/', include('markbook.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
