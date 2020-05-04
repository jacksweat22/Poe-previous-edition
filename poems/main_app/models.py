from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Poems(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  poem = models.TextField(max_length=250)
#   genre = models.Field(dont know the model for genre)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField('Posted Date')

class Meta:
  ordering = ['-date']


class Comments:
  poem = model.TextField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField(max_length=250)


class Photo(models.Model):
  url = models.CharField(max_length=200)
  poems = models.ForeignKey(Poems, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for poem_id: {self.poem_id} @{self.url}"
