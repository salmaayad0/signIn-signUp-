from django.db import models
# abstract user model from django user model
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField('admin', default=False)
    is_editor = models.BooleanField('editor', default=False)
    is_user = models.BooleanField('user', default=False)
    
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []