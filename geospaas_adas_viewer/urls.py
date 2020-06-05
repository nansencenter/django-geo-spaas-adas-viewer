from django.conf.urls import url, include

from geospaas_adas_viewer.views import AdasIndexView


app_name = 'geospaas_adas_viewer'
urlpatterns = [
    url('', adasIndexView.as_view(), name='adasindex'),
]
