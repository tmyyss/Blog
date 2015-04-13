from django.conf.urls import patterns,url

from blog.views import *

urlpatterns = patterns('',
	url(r'^$',index,name='index'),
	url(r'^list/$',list,name='list'),
	url(r'^edit/$',edit,name='edit'),
	url(r'^(?P<pk>\d+)/$',DetailView.as_view(),name='detail'),
	url(r'^update/(?P<id>\d+)$',update,name='update'),
	url(r'^remove/(?P<id>\d+)$',remove,name='remove'),
)
