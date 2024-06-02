from django.db import models

# Create your models here.

class BLOG(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.title
