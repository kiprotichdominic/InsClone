from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CreatePostForm, CreateCommentForm
from .models import Post, Comment

class HomePageView(ListView):
    model= Comment
    success_url = reverse_lazy('home')
    model = Post
    form_class= CreateCommentForm
    template_name = 'instapp/index.html'
    context_object_name = 'posts'
    ordering =['-date_posted']
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'instapp/detail.html'     
    

class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'instapp/createpost.html' 
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)