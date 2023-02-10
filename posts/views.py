from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):
    # if the methode is Post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
    # If the form is valid
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    #yes, save

    # #redirect to home
    # No, Show Error
        else:
            return HttpResponseRedirect(form.errors.as_json())
    # get all post, limit =20

    posts = Post.objects.all().order_by('-created_at')[:20]
    form = PostForm()
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    output = 'POST ID is ' + str(post_id)
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    # if the methode is Post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
    # If the form is valid
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    #yes, save

    # #redirect to home
    # No, Show Error
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, "edit.html", {'post': post})


def like(request, post_id):
    post = Post.objects.get(id=post_id)
    new_like = post.likes + 1
    post.likes = new_like
    post.save()
    return HttpResponseRedirect('/')