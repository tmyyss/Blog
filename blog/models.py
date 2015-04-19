#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Blog(models.Model):
	class Meta:
		verbose_name=u'文章'
		verbose_name_plural=u'文章'
	user=models.ForeignKey(User,verbose_name=u'作者')
	title=models.CharField(max_length=200,verbose_name=u'文章标题')
	text=models.TextField(verbose_name=u'正文内容')
	created_time=models.DateTimeField(default=timezone.now,verbose_name=u'创建时间')
	published_time=models.DateTimeField(blank=True,null=True,verbose_name=u'发布时间')
	visitors=models.IntegerField(default=0,verbose_name=u'访问量')

	def __unicode__(self):
		return self.title

class PostForm(ModelForm):
	class Meta:
		model=Blog
		fields=('title','text')
	
