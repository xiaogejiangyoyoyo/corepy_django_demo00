# from django.shortcuts import render_to_response, render
# from django.views.decorators.csrf import csrf_protect
# from blog.models import BlogPost, BlogPostForm
# from datetime import datetime
# from django.http import HttpResponseRedirect
# from django.template import RequestContext
#
#
# def create_blogpost(request):
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.timestamp = datetime.now()
#             post.save()
#     return HttpResponseRedirect('/blog/')
#
#
# def archive(request):
#     posts = BlogPost.objects.all()
#     return render(request, 'archive.html', {'posts': posts, 'form': BlogPostForm()})

from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    return render(request, 'archive.html', {'posts': posts})


def create_blogpost(request):
    if request.method == 'POST':
# def create_blogpost(request):
#     if request == 'POST':
        BlogPost(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            timestamp=datetime.now(),
            # title=123,
            # body=123123,
            # timestamp=datetime.now(),
        ).save()
    return HttpResponseRedirect('/blog/')
