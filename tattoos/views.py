from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import *  
from .serializers.common import *


class TattooList(ListAPIView):
  queryset = Tattoo.objects.all()
  serializer_class = PopulatedTattooSerializer

class TattooCreate(CreateAPIView):
  queryset = Tattoo.objects.all()
  serializer_class = TattooSerializer

class TattooUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Tattoo.objects.all()
  serializer_class = TattooSerializer

class TattooDetail(RetrieveAPIView):
  queryset = Tattoo.objects.all()
  serializer_class = PopulatedTattooSerializer


class ArtistListCreate(APIView):
    # List Authors
    def get(self, request):
        artists = Artist.objects.all()
        serialized_artists = PopulatedArtistSerializer(artists, many=True)
        return Response(data=serialized_artists.data, status=status.HTTP_200_OK)

    # Create Author
    def post(self, request):
        artist_serializer = ArtistSerializer(data=request.data)
        if artist_serializer.is_valid():
            artist_serializer.save()
            return Response(data=artist_serializer.data, status=status.HTTP_200_OK)
        return Response(data=artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistRetrieveUpdateDelete(APIView):
    def get(self, request, pk):
        artist = self.get_artist(pk=pk)
        serialized_artist = ArtistSerializer(artist)
        return Response(data=serialized_artist.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        artist_to_update = self.get_artist(pk=pk)
        updated_artist = ArtistSerializer(artist_to_update, data=request.data)
        if updated_artist.is_valid():
            updated_artist.save()
            return Response(updated_artist.data, status=status.HTTP_200_OK)
        return Response(data=updated_artist.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        artist_to_delete = self.get_artist(pk=pk)
        artist_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_artist(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        
        except Artist.DoesNotExist:
            
            raise NotFound(detail="Can't find that artist")
