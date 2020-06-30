from django.urls import path
from geospaas_adas_viewer.views import AdasIndexView
from geospaas.base_viewer.views import get_geometry_geojson

app_name = 'geospaas_adas_viewer'
urlpatterns = [
    path('', AdasIndexView.as_view(), name='adasindex'),
    path('geometry/<int:pk>', get_geometry_geojson, name='geometry_geojson')
]
