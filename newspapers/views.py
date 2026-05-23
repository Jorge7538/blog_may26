from django.shortcuts import render
from .models import blog
from django.views.generic import ListView

class PostListView(ListView):
    model = blog
    template_name = 'post_list.html'
    
