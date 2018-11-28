from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField, get_thumbnail


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    likes = models.IntegerField(blank=True, default=0)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    photo = ImageField(upload_to='photos/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_thumbnail_url(self):
        if self.photo:
            thumbnail = get_thumbnail(self.photo, '614x425', crop='center')
            return thumbnail.url
        else:
            return None
