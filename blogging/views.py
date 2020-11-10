from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader

from blogging.models import Post


def detail_view(request, post_id):
    published = Post.objects.all()
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)


def list_view(request):
    published = Post.objects.all()
    print(published)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)

