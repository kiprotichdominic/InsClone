from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.date_posted

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})