from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    post = posts.objects.all()
    return render(request, 'blog/home.html', {'posts':post})


class postsListView(ListView):
    model = posts
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5

class UserpostsListView(ListView):
    model = posts
    template_name = "blog/user-posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username= self.kwargs.get('username'))
        return posts.objects.filter(author=user).order_by('-date_posted')
        

class postsDetailView(DetailView):
    model = posts
    
class postsCreateView(LoginRequiredMixin, CreateView):
    model = posts
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class postsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = posts
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

class postsDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = posts
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request, 'blog/about.html')
