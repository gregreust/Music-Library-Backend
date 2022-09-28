from xml.dom.minidom import AttributeList
from django.db import models

class Song (models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    album = models.CharField(max_length=150)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    likes = models.IntegerField()