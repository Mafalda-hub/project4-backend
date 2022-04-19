from rest_framework import serializers

from reviews.serializers import PopulatedReviewSerializer, ReviewSerializer
from ..models import *

class TattooSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tattoo
    fields = ('__all__')

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artistfields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('__all__')

class PopulatedTattooSerializer(TattooSerializer):
  artist = ArtistSerializer()
  categories = CategorySerializer(many=True)
  reviews = PopulatedReviewSerializer(many=True)


class TattooWithCategorySerializer(TattooSerializer):
  categories = CategorySerializer(many=True)

class PopulatedArtistSerializer(ArtistSerializer):
  tattoos = TattooWithCategorySerializer(many=True)