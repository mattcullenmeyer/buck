from rest_framework import generics, filters
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

class SuggestedView(generics.RetrieveAPIView):
  queryset = models.Suggested.objects.all()
  serializer_class = serializers.SuggestedSerializer
  lookup_field = 'slug'

class AggregatedView(generics.RetrieveAPIView):
  queryset = models.School.objects.all()
  serializer_class = serializers.AggregatedSerializer
  lookup_field = 'slug'