from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(null=True, blank=True)
    body = models.TextField()
    link = models.CharField(max_length=200, default="NA")

    def __str__(self):
        return self.title

