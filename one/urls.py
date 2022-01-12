from django.urls import path
from one import views

app_name = 'one'
urlpatterns = [
  path('schools/', views.SchoolsView.as_view(), name='schools'),
  path('school/<slug>/', views.SchoolView.as_view(), name='school'),
  path('suggested/', views.SuggestedView.as_view(), name='suggested'),
  path('nearby/', views.NearbyView.as_view(), name='nearby'),
  path('aggregated/<slug>/', views.AggregatedView.as_view(), name='aggregated'),
  path('nearby/create/', views.CreateNearby.as_view(), name='nearby_create'),
]