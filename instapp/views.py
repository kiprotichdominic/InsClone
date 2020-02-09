from django.views.generic import TemplateView, ListView

from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'instapp/index.html'
     
     