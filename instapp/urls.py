from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePageView, PostDetailView

urlpatterns = [
    path('home/', HomePageView.as_view(), name ='home'),
    path('poat<int:pk>', PostDetailView.as_view(), name ='post_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)