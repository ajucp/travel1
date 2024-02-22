from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="pics")
    dis=models.TextField()

    def __str__(self):
        return self.name

class reviewer(models.Model):
    name=models.CharField(max_length=250)
    loc=models.TextField()
    disc=models.TextField()
    def __str__(self):
        return self.name

class reviews(models.Model):
    name=models.CharField(max_length=250)
    loc=models.TextField()
    disc=models.TextField()
    def __str__(self):
        return self.name