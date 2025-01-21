from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Publication
from .serializers import CategorySerializer, PublicationSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PublicAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'Это публичный маршрут!'})
    


class PublicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publication.objects.filter(is_archived=False)
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


