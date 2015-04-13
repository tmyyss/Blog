from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Blog,PostForm
from django.views import generic
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import datetime

def index(request):

	blog_list=Blog.objects.all().order_by('-published_time')
	paginator=Paginator(blog_list,3)
	
	page=request.GET.get('page')

	try:
		blogs=paginator.page(page)
	except PageNotAnInteger:
		blogs=paginator.page(1)
	except EmptyPage:
		blogs=paginator.page(paginator.num_pages)

	return render(request,'blog/index.html',{'blogs':blogs})
	
def list(request):
	blog_list=Blog.objects.all()
        paginator=Paginator(blog_list,10)

        page=request.GET.get('page')

        try:
                blogs=paginator.page(page)
        except PageNotAnInteger:
                blogs=paginator.page(1)
        except EmptyPage:
                blogs=paginator.page(paginator.num_pages)

        return render(request,'blog/blog_list.html',{'blogs':blogs})

class DetailView(generic.DetailView):
	model=Blog
	template_name='blog/detail.html'	

def edit(request):
	if request.method=='POST':
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.user=request.user
			post.created_time=datetime.datetime.now()
			post.published_time=datetime.datetime.now()
			post.save()
			return render(request,'blog/detail.html',{'blog':post})
	else:
		form=PostForm()
	return render(request,'blog/edit.html',{'form':form})

def update(request,id):
	post=get_object_or_404(Blog,pk=id)
	if request.method=='POST':
                form=PostForm(request.POST,instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.user=request.user
			post.save()
			return render(request,'blog/detail.html',{'blog':post})
	else:
		form=PostForm(instance=post)
        return render(request,'blog/edit.html',{'form':form})
def remove(request,id):
	blog=get_object_or_404(Blog,pk=id)
	Blog.objects.filter(pk=id).delete()
        return render(request,'blog/after_remove.html',{})


