from django.shortcuts import render
from .models import blog
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = blog
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = blog
    template_name = 'post_detail.html'

