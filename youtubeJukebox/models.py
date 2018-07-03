from django.db import models

# Create your models here.
class Video(models.Model):
	url = models.URLField()
	videoId = models.CharField(max_length=100,unique=True)
	vote = models.IntegerField(default=0)

	def __str__(self):
		return self.videoId

class User(models.Model):
    user = models.CharField(max_length=100,unique=True)
    user_id = models.CharField(max_length=100,unique=True)

    def is_slacked(self):
        return self.access_token
