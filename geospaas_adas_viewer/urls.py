from django.urls import path
from geospaas_adas_viewer.views import AdasIndexView

app_name = 'geospaas_adas_viewer'
urlpatterns = [
    path('', AdasIndexView.as_view(), name='adasindex'),
]
