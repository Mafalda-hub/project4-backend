from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers.common import *

# Create your views here.

class ListView(APIView):
  def get(self, _request):
    tattoos = Tattoo.objects.all()
    serializer = TattooSerializer(tattoos, many=True)
    return Response(serializer.data)