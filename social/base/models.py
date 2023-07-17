from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, blank=True, null=True, default="")
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500,blank=True, null=True, default="" )

    def __str__(self):
        return self.title   

class Comment(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    related_post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.related_post}: {self.comment}'