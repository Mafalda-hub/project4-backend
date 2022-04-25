from django.db import models


class Artist(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Tattoo(models.Model):
  name = models.CharField(max_length=50)
  artist = models.ForeignKey(Artist, related_name='tattoos', on_delete=models.CASCADE, null=True)
  description = models.CharField(max_length=200)
  image = models.CharField(max_length=200, blank=True)
  category = models.ForeignKey(Category, related_name='tattoos', on_delete=models.CASCADE, blank=True)

  def __str__(self):
    return self.name