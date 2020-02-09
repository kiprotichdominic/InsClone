from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePageView, PostDetailView, PostCreateView

urlpatterns = [
    path('home/', HomePageView.as_view(), name ='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name ='post_detail'),
    path('post/new', PostCreateView.as_view(), name ='post_create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)