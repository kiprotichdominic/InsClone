from django.views.generic import TemplateView, ListView, DetailView

from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'instapp/index.html'
    context_object_name = 'posts'
    ordering =['date_posted']
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'instapp/detail.html'     