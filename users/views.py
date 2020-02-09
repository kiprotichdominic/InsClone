from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
# from django.contrib.auth.models import User


# from .models import Image

# class PostListView(ListView):
#     model = Image
#     template_name = 'instapp/index.html'

class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    
class ProfilePageView(LoginRequiredMixin ,TemplateView):
    template_name = 'users/profile.html'
    
@login_required
def ProfileEditPageView(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profileedit.html', context)
    
# class ProfileEditPageView(LoginRequiredMixin,FormView):
#     # form_class = ProfileUpdateForm
#     form_class = UserUpdateForm 
#     success_url = reverse_lazy('profile')
#     template_name = 'users/profileedit.html'
    

# class PostCreateView(CreateView):
#     model = Image
#     template_name = 'instapp/newpost.html'
#     fields = ['image','caption']

# class PostDetailView(DetailView):
#     model = Image
#     template_name = 'instapp/imagedetail.html'