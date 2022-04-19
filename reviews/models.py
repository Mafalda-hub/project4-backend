
from django.db import models
from django.contrib.auth import get_user_model
from tattoos.models import Tattoo
from jwt_auth.models import CustomUser

# this is the user that uses a build in Django method  
# CustomUser = get_user_model()

class Review(models.Model):

  text = models.TextField(max_length=300)
  # owner = models.ForeignKey(CustomUser, related_name ='reviews', on_delete= models.CASCADE )
  tattoo = models.ForeignKey(Tattoo, related_name='reviews', on_delete=models.CASCADE )
  created_date = models.DateField(auto_now_add = True)

  def __str__(self):
    return f'{self.tattoo} {self.tattoo.artist} - {self.text} on {self.created_date}'