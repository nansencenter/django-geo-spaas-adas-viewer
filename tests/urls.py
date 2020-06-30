from django.urls import include, path

urlpatterns = [
    path('', include('geospaas_adas_viewer.urls')),
]
