from django.conf.urls import include, url
from django.contrib import admin
from views import IndexListView
from views import PostDetailView
from views import TagPostListView
from views import CategoryPostListView
from views import TagsListView
from views import ArchivesListView

urlpatterns = [
    # Examples:
    url(r'^$', IndexListView.as_view(), name='home'),
    url(r'^post/(?P<slug>.*)$', PostDetailView.as_view(), name='post'),
    url(r'^tag/(?P<item_name>.*)$', TagPostListView.as_view(), name='tags'),
    url(r'^category/(?P<item_name>.*)$', CategoryPostListView.as_view(), name='category'),
    url(r'^tags', TagsListView.as_view(), name='tags'),
    url(r'^archives', ArchivesListView.as_view(), name='tags'),
    #url(r'^blog/', include('markbook.urls')),

    #url(r'^admin/', include(admin.site.urls)),
]
