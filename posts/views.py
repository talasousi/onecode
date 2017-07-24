from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def post_create(request):
	post_list = Post.objects.all()
	content = Post.objects.all().first()
	context = {
		"title": "Post Page",
		"content": content,
		"random_numbers": random.randint(1,1000),
		
		"list": post_list,
	}
	return render(request, 'create.html', context)

def post_update(request):
	return HttpResponse("<h1> Update <h1>")

def post_delete(request):
	return HttpResponse("<h1> Delete <h1>")

def post_list(request):
	obj_list = Post.objects.all()
	context = {
		"post_list": obj_list,
	}

	return render(request, 'post_list.html', context)

def post_detail(request, post_id):
	obj = get_object_or_404(Post, id=post_id)
	context = {
		"instance": obj,
	}
	return render(request, 'post_detail.html', context)