# from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blogging.models import Post


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'


class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list.html'

    def get_queryset(self):
        queryset = Post.objects.order_by('-published_date').exclude(published_date__exact=None)
        return queryset


