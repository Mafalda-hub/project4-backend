from django.db import models

# Create your models here.

class Tattoo(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  image = models.CharField(max_length=200, blank=True)

  def __str__(self):
    return self.name