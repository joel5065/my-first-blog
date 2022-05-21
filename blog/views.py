from multiprocessing import context
from os import rename
from django import template
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('created_date')
    template = loader.get_template('blog/post_list.html')
    context = {
        'posts': posts,
        }
    return HttpResponse(template.render(context, request))

def post_detail(request, pk):
    post_detail = Post.objects.get(pk=pk)
    template = loader.get_template('blog/post_detail.html')
    context = {
        'post_detail': post_detail,
    }
    return HttpResponse(template.render(context, request))

    