from django.db import models
from django.conf import settings

class station(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    main_image = models.ImageField(upload_to='static/img/')
    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)

class fact(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    main_image = models.ImageField(upload_to='static/img/')
    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)