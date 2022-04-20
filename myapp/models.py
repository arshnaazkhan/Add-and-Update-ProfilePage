from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100, blank=True)

    email = models.EmailField(max_length=255, unique=True)

    contact_no = models.CharField(max_length=17, unique=True, null=False, blank=False)

    password = models.CharField(max_length=100)  
    
    def __str__(self):  
        return self.full_name
  