from django.db import models

# Create your models here.
class Blog(models.Model):
    title =  models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    blog_image = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=2000)
