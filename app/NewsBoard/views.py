import http.client

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View
from django import http

from .models import Post
from .forms import PostForm


class MainPage(View):
    """Home-Main page of the web-site"""
    template_name = 'NewsBoard/main_page.html'

    def get(self, request):
        context = dict()
        context['username'] = request.user.username

        return render(request, self.template_name, context)


# ===================== CRUD Post MODEL ========================
class PostList(ListView):
    """List of all posts on the web-site"""
    model = Post
    ordering = '-date_added'
    template_name = 'NewsBoard/post_list.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    """Selected post by posts id"""
    model = Post
    context_object_name = 'post'
    template_name = 'NewsBoard/post_detail.html'


class PostCreate(CreateView):
    """Created new post in web-site"""
    model = Post
    form_class = PostForm
    template_name = 'NewsBoard/post_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(PostCreate, self).form_valid(form)


class PostDelete(DeleteView):
    """Delete selected post in web-site"""
    model = Post
    template_name = 'NewsBoard/post_delete.html'
    success_url = reverse_lazy('NewsBoard:main-page')

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user == object.author:
            return super().get(self, request, *args, **kwargs)
        else:
            raise http.Http404


class PostUpdate(UpdateView):
    """Update-edit selected post in web-site"""
    model = Post
    form_class = PostForm
    template_name = 'NewsBoard/post_create.html'

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user == object.author:
            return super().get(self, request, *args, **kwargs)
        else:
            raise http.Http404
# ===============================================================
