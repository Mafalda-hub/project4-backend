
from django.urls import path
from reviews.views import ReviewCreate


urlpatterns= [
  path('create/', ReviewCreate.as_view()),
]