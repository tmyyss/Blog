from django.conf.urls import patterns,url

from blog.views import *

urlpatterns = patterns('',
	url(r'^$',index,name='index'),
	url(r'^list/$',list,name='list'),
	url(r'^edit/$',edit,name='edit'),
	url(r'^blog/(?P<pk>\d+)/$',detail,name='detail'),
	url(r'^blog/(?P<pk>\d+)/update/$',update,name='update'),
	url(r'^blog/(?P<pk>\d+)/remvoe/$',remove,name='remove'),
	url(r'^aboutme/$',aboutme,name='aboutme')
)
