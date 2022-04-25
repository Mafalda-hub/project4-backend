from rest_framework import serializers

from reviews.serializers import PopulatedReviewSerializer
from ..models import *

# !TATTOOS

class TattooSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tattoo
    fields = ('__all__')

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('__all__')

class PopulatedCategorySerializer(CategorySerializer):
  tattoos = TattooSerializer(many= True)

class PopulatedTattooSerializer(TattooSerializer):
  artist = ArtistSerializer()
  category = CategorySerializer(many=True)
  reviews = PopulatedReviewSerializer(many=True)


class TattooWithCategoriesSerializer(TattooSerializer):
  categories = CategorySerializer(many=True)

class PopulatedArtistSerializer(ArtistSerializer):
  tattoos = TattooWithCategoriesSerializer(many=True)