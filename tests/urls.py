from django.urls import include, path

""" NB: Order of paths is important here!

geospaas_adas_viewer.urls points to AdasIndexView
geospaas.base_viewer.urls point to:
     ''             - IndexView
     'geometry/'    - get_geometry_geojson

If order is reverse (base_viewr first), then AdasIndexView is not used.
"""

urlpatterns = [
    path('', include('geospaas_adas_viewer.urls')),
    path('', include('geospaas.base_viewer.urls')),
]
