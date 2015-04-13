from django.contrib import admin
from models import Blog

class Blogadmin(admin.ModelAdmin):
	list_display=('title','created_time','user','published_time')
	list_filter=['created_time']

admin.site.register(Blog,Blogadmin)
