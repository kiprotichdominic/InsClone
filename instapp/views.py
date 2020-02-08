from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import generic
from .models import Image

class PostListView(ListView):
    model = Image
    template_name = 'instapp/index.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
class PostCreateView(CreateView):
    model = Image
    template_name = 'instapp/post_new.html'
    fields = '__all__'

class PostDetailView(DetailView):
    model = Image
    template_name = 'instapp/imagedetail.html'