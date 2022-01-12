from django.contrib import admin
from one import models

class NearbyAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)
  list_display = ('id', 'target', 'nearby', 'distance',)
  search_fields = ('target__name',)

admin.site.register(models.School)
admin.site.register(models.Ratings)
admin.site.register(models.Statistics)
admin.site.register(models.Suggested)
admin.site.register(models.Nearby, NearbyAdmin)