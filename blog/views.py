from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     context = {
#         'posts' : Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


def my_posts(request):
    context = {
        'posts': Post.objects.all().filter(author=request.user)
    }
    return render(request, 'blog/my_posts.html', context)


class MyPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/my_posts.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().filter(author=self.request.user).order_by('-date_posted')
        return context


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title' , 'content', 'x', 'y']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title' , 'content','x', 'y']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/post/my_posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
