from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=150)
    img=models.ImageField(upload_to='pics')
    desc = models.TextField()


def __str__(self):
    return self.name
#
# class Picture(models.Model):
#namee = models.CharField(max_length=150,default='dd')
    # image = models.ImageField(upload_to='pt',default='path/to/image.png')
    # descr = models.TextField(default='he1')
# def __str__(self):
#     return self.namee
