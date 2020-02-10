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
        return self.caption

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    

# class Comment(models.Model):
#     post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)


#     def __str__(self):
#         return self.text
    
    
# class Like(models.Model):
#     user = models.ForeignKey(User)
#     post = models.ForeignKey(Post)
#     created = models.DateTimeField(auto_now_add=True)