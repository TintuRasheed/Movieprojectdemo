from django.db import models

# Create your models here.

class Movie(models.Model):
    Name=models.CharField(max_length=100)
    Desc=models.TextField()
    year=models.IntegerField()
    Img=models.ImageField(upload_to='Gallery')
    def __str__(self):
        return self.Name