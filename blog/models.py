from django.db import models
from django.utils import timezone

'''
    - fields , options 
    - validation
    - html widget
'''
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=30000)
    create_date = models.DateTimeField(default=timezone.now())
    draft = models.BooleanField(default=True)
