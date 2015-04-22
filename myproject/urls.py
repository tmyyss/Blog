from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
	url(r'',include('blog.urls',namespace='blog')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$','django.contrib.auth.views.login'),
	url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'next_page':'/'}),
	url(r'^ckeditor/',include('ckeditor.urls'))
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
