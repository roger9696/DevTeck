from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.

class Videos(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(default='', editable=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(default='fallback.png', blank=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate slug from title if not provided
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True)
    number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Profile for {self.user.username}'



