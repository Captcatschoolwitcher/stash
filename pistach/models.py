
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #content = models.TextField()
    image = models.ImageField()
    link = models.TextField()
    #created_at = models.DateField(default=timezone.now)
    #tag = models.CharField(max_length=200)

    def __str__(self):
        return self.title


