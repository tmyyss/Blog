#!/usr/bin/python
#-*-encoding:utf-8 -*-

from models import Blog
from haystack import indexes

class BlogIndex(indexes.SearchIndex,indexes.Indexable):
	text=indexes.CharField(document=True,use_template=True)
	title=indexes.CharField(model_attr='title')
	
	def get_model(self):
		return Blog
	def index_queryset(self,using=None):
		return self.get_model().objects.all()
