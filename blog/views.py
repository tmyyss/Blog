from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Blog,PostForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
import datetime

def index(request):

	mblogs=Blog.objects.all().order_by('-visitors')[:5]
	blog_list=Blog.objects.all().order_by('-published_time')
	paginator=Paginator(blog_list,3)
	
	page=request.GET.get('page')

	try:
		blogs=paginator.page(page)
	except PageNotAnInteger:
		blogs=paginator.page(1)
	except EmptyPage:
		blogs=paginator.page(paginator.num_pages)

	return render(request,'blog/index.html',{'blogs':blogs,'mblogs':mblogs})
	
def list(request):
	blog_list=Blog.objects.all().order_by('-published_time')
	mblogs=Blog.objects.all().order_by('-visitors')[:5]
        paginator=Paginator(blog_list,10)

        page=request.GET.get('page')

        try:
                blogs=paginator.page(page)
        except PageNotAnInteger:
                blogs=paginator.page(1)
        except EmptyPage:
                blogs=paginator.page(paginator.num_pages)

        return render(request,'blog/blog_list.html',{'blogs':blogs,'mblogs':mblogs})

def detail(request,pk):
	post=get_object_or_404(Blog,pk=pk)
	mblogs=Blog.objects.all().order_by('-visitors')[:5]
	post.visitors=post.visitors+1
	post.save()
	return render(request,'blog/detail.html',{'blog':post,'mblogs':mblogs})	

@login_required
def edit(request):
	mblogs=Blog.objects.all().order_by('-visitors')[:5]
	if request.method=='POST':
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.user=request.user
			post.created_time=datetime.datetime.now()
			post.published_time=datetime.datetime.now()
			post.save()
			return redirect(detail,pk=post.pk)
	else:
		form=PostForm()
	return render(request,'blog/edit.html',{'form':form,'mblogs':mblogs})

@login_required
def update(request,pk):
	mblogs=Blog.objects.all().order_by('-visitors')[:5]
	post=get_object_or_404(Blog,pk=pk)
	if request.method=="POST":
                form=PostForm(request.POST,instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.user=request.user
			post.save()
			return redirect(detail,pk=post.pk)
	else:
		form=PostForm(instance=post)
        return render(request,'blog/update.html',{'form':form,'mblogs':mblogs})

@login_required
def remove(request,pk):
	mblogs=Blog.objects.all().order_by('-visitors')[:5]
	blog=get_object_or_404(Blog,pk=pk)
	Blog.objects.filter(pk=pk).delete()
        return render(request,'blog/after_remove.html',{'mblogs':mblogs})

def aboutme(request):	
	mblogs=Blog.objects.all().order_by('-visitors')[:5]
	return render(request,'blog/aboutme.html',{'mblogs':mblogs})
