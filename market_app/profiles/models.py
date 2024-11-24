from django.contrib.auth import get_user_model
from django.db import models

class Profile(models.Model):
    author = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)
    bio = models.TextField()
    
