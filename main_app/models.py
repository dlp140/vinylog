from pyexpat import model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Record(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    notes = models.CharField(max_length=200)
    condition = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.artist + " - " + self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'record_id': self.id})

class Collection(models.Model):
    date_added = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record = models.ManyToManyField(Record)

    class Meta:
        ordering = ['-date_added']