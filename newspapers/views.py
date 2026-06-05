from django.shortcuts import render
from .models import blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(LoginRequiredMixin, ListView):
    model = blog
    template_name = 'post_list.html'

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

class PostUpdateView(UpdateView):
    model = blog
    template_name = 'post-update.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = blog
    template_name = 'post-delete.html'
    success_url = reverse_lazy('post_list')

class PostLogoutView(LogoutView):
    template_name = 'Logout.html'