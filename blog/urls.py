from django.conf.urls import patterns,url,include
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^list/$',views.list,name='list'),
	url(r'^edit/$',views.edit,name='edit'),
	url(r'^blog/(?P<pk>\d+)/$',views.detail,name='detail'),
	url(r'^blog/(?P<pk>\d+)/update/$',views.update,name='update'),
	url(r'^blog/(?P<pk>\d+)/remvoe/$',views.remove,name='remove'),
	url(r'^aboutme/$',views.aboutme,name='aboutme'),
	url(r'^search/',views.search,name='search'),
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
