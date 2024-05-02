from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=30)
    
    labels = [
        {first_name : 'First Name'}
    ]
    
    def __str__(self):
        return self.first_name
