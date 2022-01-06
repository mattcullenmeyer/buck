from rest_framework import serializers
from one import models

class SchoolSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.School
    fields = '__all__'

class RatingsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Ratings
    fields = '__all__'

class StatisticsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Statistics
    fields = '__all__'

class SuggestedSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Suggested
    fields = '__all__'

class AggregatedSerializer(serializers.ModelSerializer):
  ratings = RatingsSerializer()
  statistics = StatisticsSerializer()

  class Meta:
    model = models.School
    fields = '__all__'