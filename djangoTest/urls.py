from django.conf.urls.defaults import patterns, include, url
from myBlog.views import createPost,myPostList,postDetail
from myBlog.models import Post
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^posts/$', myPostList.as_view()),
    url(r'^posts/(?P<pk>[a-zA-Z0-9]+)/',postDetail.as_view(), name='post_detail'),#,{'template_name':'rest_framework/api_1.html'}),  
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    # Examples:
    # url(r'^$', 'djangoTest.views.home', name='home'),
    # url(r'^djangoTest/', include('djangoTest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
