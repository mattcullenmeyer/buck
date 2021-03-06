from rest_framework import generics, filters, permissions, pagination
from one import serializers, models

class SchoolsView(generics.ListAPIView):
  queryset = models.School.objects.all()
  serializer_class = serializers.SchoolSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['name']

class SchoolView(generics.RetrieveAPIView):
  queryset = models.School.objects.all()
  serializer_class = serializers.SchoolSerializer
  lookup_field = 'slug'

class SuggestedView(generics.ListAPIView):
  queryset = models.Suggested.objects.all()
  serializer_class = serializers.SuggestedSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['suggest__slug']

class CustomPagination(pagination.CursorPagination):
  page_size = 10
  ordering = 'distance'

class NearbyView(generics.ListAPIView):
  queryset = models.Nearby.objects.all()
  serializer_class = serializers.NearbySerializer
  pagination_class = CustomPagination
  filter_backends = [filters.SearchFilter]
  search_fields = ['target__slug']

class CreateNearby(generics.CreateAPIView):
  queryset = models.Nearby.objects.all()
  serializer_class = serializers.CreateNearbySerializer
  permission_classes = [permissions.IsAdminUser]

class AggregatedView(generics.RetrieveAPIView):
  queryset = models.School.objects.all()
  serializer_class = serializers.AggregatedSerializer
  lookup_field = 'slug'