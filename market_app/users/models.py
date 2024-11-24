from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):   
    REQUIRED_FIELDS = ['email']
    # unnecessary fields now 
    groups = None
    user_permissions = None
    
    # moved to Profile model
    first_name = None
    last_name = None