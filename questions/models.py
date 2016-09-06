from django.db import models
from account.models import MyUser


from django.db import models

# Create your models here.
class Popper(models.Model):
    title = models.CharField(max_length = 100, default = '')
    text = models.TextField(max_length = 1024, default = '')
    rate = models.TextField(max_length = 1024, default = '')
    profile_pic = models.ImageField( null=True, blank=True)
    def __str__(self):
        return self.title
class Candle(models.Model):
    title = models.CharField(max_length = 100, default = '')
    text = models.TextField(max_length = 1024, default = '')
    rate = models.TextField(max_length = 1024, default = '')
   
    profile_pic = models.ImageField( null=True, blank=True)
    def __str__(self):
        return self.title
class Balloon(models.Model):
    title = models.CharField(max_length = 100, default = '')
    text = models.TextField(max_length = 1024, default = '')
    rate = models.TextField(max_length = 1024, default = '')
    
    profile_pic = models.ImageField( null=True, blank=True)
    def __str__(self):
        return self.title
class Knife_Caketag(models.Model):
    title = models.CharField(max_length = 100, default = '')
    text = models.TextField(max_length = 1024, default = '')
    rate = models.TextField(max_length = 1024, default = '')
    
    profile_pic = models.ImageField( null=True, blank=True)
    def __str__(self):
        return self.title
class Prop_Decoration(models.Model):
    title = models.CharField(max_length = 100, default = '')
    text = models.TextField(max_length = 1024, default = '')
    rate = models.TextField(max_length = 1024, default = '')
   
    profile_pic = models.ImageField( null=True, blank=True)
    def __str__(self):
        return self.title

class Cap(models.Model):
    title = models.CharField(max_length = 100, default = '')
    text = models.TextField(max_length = 1024, default = '')
    rate = models.TextField(max_length = 1024, default = '')
    
    profile_pic = models.ImageField( null=True, blank=True)
    def __str__(self):
        return self.title
class Crown(models.Model):
    title = models.CharField(max_length = 100, default = '')
    text = models.TextField(max_length = 1024, default = '')
    rate = models.TextField(max_length = 1024, default = '')
    
    profile_pic = models.ImageField( null=True, blank=True)
    def __str__(self):
        return self.title
class New_Arrival(models.Model):
    title = models.CharField(max_length = 100, default = '')
    text = models.TextField(max_length = 1024, default = '')
    rate = models.TextField(max_length = 1024, default = '')
    
    profile_pic = models.ImageField( null=True, blank=True)
    def __str__(self):
        return self.title