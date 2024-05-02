from django.db import models
from musician.models import Musician
import datetime
# Create your models here.

RATINGS = [
    ('1*' , '1*'),
    ('2*' , '2*'),
    ('3*' , '3*'),
    ('4*' , '4*'),
    ('5*' , '5*'),
]

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician , on_delete=models.CASCADE)
    realase_date = models.DateField(default=datetime.datetime.now())
    ratings = models.CharField(max_length=20 , choices=RATINGS)
    
    def __str__(self):
        return self.album_name
    
