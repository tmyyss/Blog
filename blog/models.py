#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Blog(models.Model):
	user=models.ForeignKey(User,verbose_name=u'作者')
	title=models.CharField(max_length=200,verbose_name=u'文章标题')
	text=models.TextField(verbose_name=u'正文内容')
	created_time=models.DateTimeField(default=timezone.now,verbose_name=u'创建时间')
	published_time=models.DateTimeField(blank=True,null=True,verbose_name=u'发布时间')

	def __unicode__(self):
		return self.title

class PostForm(ModelForm):
	class Meta:
		model=Blog
		fields=('title','text')
	
