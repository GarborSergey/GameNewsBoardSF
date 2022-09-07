import http.client

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, path, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View
from django import http

from .models import Post, Message
from .forms import PostForm, MessageForm


class MainPage(View):
    """Home-Main page of the web-site"""
    template_name = 'NewsBoard/main_page.html'

    def get(self, request):
        context = dict()

        return render(request, self.template_name, context)


# ===================== CRUD Post MODEL ========================
class PostList(ListView):
    """List of all posts on the web-site"""
    paginate_by = 5
    model = Post
    ordering = '-date_added'
    template_name = 'NewsBoard/post_list.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    """Selected post by posts id"""
    model = Post
    context_object_name = 'post'
    template_name = 'NewsBoard/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(post=self.kwargs['pk'], public=True)
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    """Created new post in web-site"""
    model = Post
    form_class = PostForm
    template_name = 'NewsBoard/post_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(PostCreate, self).form_valid(form)


class PostDelete(LoginRequiredMixin, DeleteView):
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


class PostUpdate(LoginRequiredMixin, UpdateView):
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


@login_required
def add_post_to_favorites(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    if user == post.author:
        raise http.Http404
    post.liked.add(user)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_post_from_favorites(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    if user not in post.liked.all():
        raise http.Http404
    post.liked.remove(user)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def message_to_post(request, pk):
    sender = request.user
    post = Post.objects.get(id=pk)
    recipient = post.author

    if sender == recipient:
        raise http.Http404

    if request.method == 'POST':
        form_message = MessageForm(request.POST)
        if form_message.is_valid():
            message = form_message.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            message.post = post
            message.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form_message = MessageForm()

    context = {
        'form': form_message,
        'post': post,
    }
    return render(request, 'NewsBoard/message_to_post.html', context)


@login_required
def all_my_posts(request):
    user = request.user
    posts = Post.objects.filter(author=user).order_by('-date_added')
    context = {
        'posts': posts
    }
    return render(request, 'NewsBoard/my_posts.html', context)


@login_required
def message_list_on_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.user != post.author:
        raise http.Http404

    messages = Message.objects.filter(post=post).order_by('-date_added')

    context = {
        'post_title': post.title,
        'messages': messages
    }

    return render(request, 'NewsBoard/message_list.html', context)


@login_required
def message_delete(request, pk):
    message = Message.objects.get(id=pk)
    if message.recipient != request.user:
        raise http.Http404

    message.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def message_to_publish(request, pk):
    message = Message.objects.get(id=pk)
    if message.recipient != request.user:
        raise http.Http404

    if message.public:
        message.public = False
    else:
        message.public = True

    message.save()
    return redirect(request.META.get('HTTP_REFERER'))
