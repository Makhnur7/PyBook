from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
# from rest_framework.response import Response
from django_filters import rest_framework as filters

from .models import Category, Publication
from .serializers import CategorySerializer, PublicationSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import CategoryFilter, PublicationFilter


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CategoryFilter

class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class PublicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publication.objects.filter(is_archived=False)
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly ]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PublicationFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PublicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


