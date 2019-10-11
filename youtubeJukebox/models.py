from django.db import models

# Create your models here.


class Video(models.Model):
    url = models.URLField()
    videoId = models.CharField(max_length=100, unique=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.videoId


class User(models.Model):
    user = models.CharField(max_length=100, unique=True)
    user_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.user_id


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.user, self.video
