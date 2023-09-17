from django.db import models
from django.utils import timezone

# Create your models here.

class District(models.Model):
     name = models.CharField(max_length=200)
     description = models.TextField()
     created = models.DateTimeField(default=timezone.now, null=True, blank=True)
     updated = models.DateTimeField(auto_now=True, null=True, blank=True)

     def __str__(self):
          return self.name


class Township(models.Model):
     district = models.ForeignKey(District, on_delete=models.CASCADE)
     name = models.CharField(max_length=200)
     description = models.TextField()
     image = models.ImageField(upload_to='township-image')
     location = models.CharField(max_length=200, blank=True, null=True)
     created = models.DateTimeField(default=timezone.now, null=True, blank=True)
     updated = models.DateTimeField(auto_now=True, null=True, blank=True)

     def __str__(self):
          return self.name


class Village(models.Model):
     township = models.ForeignKey(Township, on_delete=models.CASCADE)
     name = models.CharField(max_length=200)
     description = models.TextField()
     image = models.ImageField(upload_to='village-image')
     location = models.CharField(max_length=200, blank=True, null=True)
     created = models.DateTimeField(default=timezone.now, null=True, blank=True)
     updated = models.DateTimeField(auto_now=True, null=True, blank=True)
     
     def __str__(self):
          return self.name

class Ward(models.Model):
     township = models.ForeignKey(Township, on_delete=models.CASCADE)
     name = models.CharField(max_length=200)
     description = models.TextField()
     image = models.ImageField(upload_to='ward-image')
     location = models.CharField(max_length=200, blank=True, null=True)
     created = models.DateTimeField(default=timezone.now, null=True, blank=True)
     updated = models.DateTimeField(auto_now=True, null=True, blank=True)
     
     def __str__(self):
          return self.name


     
class Category(models.Model):
     name = models.CharField(max_length=200)
     image = models.ImageField(upload_to = 'picture')

     def __str__(self):
          return self.name