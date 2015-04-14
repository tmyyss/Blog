from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$','blog.views.index'),
	url(r'^index','blog.views.index'),	
	url(r'^blogs/', include('blog.urls',namespace='blogs')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$','django.contrib.auth.views.login'),
	url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'next_page':'/'}),
)
