from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib	import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

#def post_create(request):
#	content = Post.objects.all().first()
#	context = {
#		"title": "Post Page",
#		"content": content,
##		"list": post_list,
#	}
#	return render(request, 'create.html', context)

def post_update(request, post_id):
	post_object = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None, request.FILES or None, instance=post_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Post updated")
		return redirect("posts:list")
	context = {
		"form": form,
		"post_object": post_object,
	}

	return render(request, 'post_update.html', context)

def post_delete(request, post_id):
	Post.objects.get(id=post_id).delete()
	messages.warning(request, "message deleted")
	return redirect("posts:list")

def post_list(request):
    obj_list = Post.objects.all()

    paginator = Paginator(obj_list, 4) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objs = paginator.page(paginator.num_pages)

    context = {
    "post_list": objs,
    }

    return render(request, 'post_list.html', context)

def post_detail(request, post_id):
	obj = get_object_or_404(Post, id=post_id)
	context = {
		"instance": obj,
	}
	return render(request, 'post_detail.html', context)

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Post created")
		return redirect("posts:list")
	context = {
		"form": form,
	}

	return render(request, 'post_create.html', context)