from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'base.html'
    context_object_name = 'posts'
