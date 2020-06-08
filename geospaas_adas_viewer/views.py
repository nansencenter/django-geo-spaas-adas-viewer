from geospaas.base_viewer.views import IndexView
from geospaas_adas_viewer.forms import ADASSearchForm

class AdasIndexView(IndexView):
    """ The class-based view for processing both GET and POST methods of basic version of viewer """
    form_class = ADASSearchForm
    viewname = 'adasindex'
