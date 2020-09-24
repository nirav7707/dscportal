from django.db import models

# Create your models here.
class Datamodel(models.Model):
    name=models.CharField(max_length=200,null=True)
    category=models.CharField(max_length=5,blank=True)
    description=models.TextField()
    datafile=models.FileField()
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class DoneEvents(models.Model):
    name=models.CharField(max_length=200,null=True)
    description=models.TextField()
    image=models.ImageField()
    registration=models.URLField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    event_date=models.DateTimeField(null=True)
    upcoming=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Showcase(models.Model):
    image1=models.ImageField()
    image2=models.ImageField()
    image3=models.ImageField()
