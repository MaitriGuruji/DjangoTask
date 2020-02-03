from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    username=models.EmailField(unique=True)
    phone_no = models.CharField(null=True,max_length=10,blank=True)
    image = models.ImageField(null=True,upload_to='image/',default="image/happycolors.jpg")


class UsrPost(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default=1,null=True)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_details')


class LikePost(models.Model):
    post = models.ForeignKey('UsrPost', on_delete=models.CASCADE, related_name='likes')
    person = models.CharField(max_length=200)


class Comment(models.Model):
    post = models.ForeignKey('UsrPost', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class UsrReg(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    phone_no = models.CharField(null=True,max_length=10,blank=True)
    image = models.ImageField(null=True,default='E:\wallpapers\happycolors.jpg',upload_to='images/')