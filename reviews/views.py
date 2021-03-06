from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from reviews.serializers import ReviewSerializer


class ReviewCreate(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        request.data['owner'] = request.user.id
        review_serializer = ReviewSerializer(data= request.data)
        if review_serializer.is_valid():
          review_serializer.save()
          return Response(data= review_serializer.data, status = status.HTTP_201_CREATED)
        return Response (data = review_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

