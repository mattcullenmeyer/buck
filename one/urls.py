from django.urls import path
from one import views

app_name = 'one'
urlpatterns = [
  path('schools/', views.SchoolsView.as_view(), name='schools'),
  path('school/<slug>/', views.SchoolView.as_view(), name='school'),
  path('suggested/<slug>/', views.SuggestedView.as_view(), name='suggested'),
  path('aggregated/<slug>/', views.AggregatedView.as_view(), name='aggregated'),
]