from django.urls import path
from .views import *

urlpatterns = [
    # Generic views for books
    path('tattoos/', TattooList.as_view()),
    path('tattoos/create/', TattooCreate.as_view()),

    path('tattoos/<int:pk>/', TattooUpdateDestroy.as_view()),

    path('tattoos/detail/<int:pk>/', TattooDetail.as_view()),

    path('artists/', ArtistListCreate.as_view()),
    path('artists/<int:pk>/',ArtistRetrieveUpdateDelete.as_view()),

]
