from django.urls import path
from .views import SignUpView, PostCreateView, PostListView, PostDetailView

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('image/new', PostCreateView.as_view(), name ='new_image'),
    path('image/<int:pk>', PostDetailView.as_view(),name='image_detail'),
    path('home/', PostListView.as_view(), name = 'home'),
]
