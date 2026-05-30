from django.shortcuts import render
from .models import blog
from django.views.generic import ListView, DetailView, CreateView

class PostListView(ListView):
    model = blog
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = blog
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = blog
    template_name = 'post-create.html'
    fields = ['title', 'content', 'author']