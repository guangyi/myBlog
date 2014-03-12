from django.conf.urls.defaults import patterns, include, url
from myBlog.views import postList,postDetail, userList, userPostList
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # call index.html, so in Angular can use ng-view
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^posts/$', postList.as_view(), name = 'post_list'),
    url(r'^posts/(?P<pk>[a-zA-Z0-9]+)/',postDetail.as_view(), name='post_detail'),#,{'template_name':'rest_framework/api_1.html'}),     

    url(r'^user/$', userList.as_view(), name='user_list'),
    url(r'user/(?P<name>[0-9a-zA-Z_+]+)/$',userList.as_view(),name='singel_user_list'),
    url(r'^user/(?P<name>[0-9a-zA-Z_-]+)/posts/$',userPostList.as_view(), name='user_post_list'),
    #url(r'^user/(?P<name>[0-9a-zA-Z_-]+)/posts/(?P<pk>[a-zA-Z0-9]+)/', postDetail.as_view(), name='user_post_detail'),
    
    # Examples:
    # url(r'^$', 'djangoTest.views.home', name='home'),
    # url(r'^djangoTest/', include('djangoTest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('', 
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), )