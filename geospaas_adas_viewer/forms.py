from django.contrib.gis import forms

from geospaas.base_viewer.forms import BaseSearchForm


class ADASSearchForm(BaseSearchForm):
    """ Form with extended searching capabilities for ADAS """
    nameparameters = forms.CharField(
        required=False, label='name (or part of the name) of parameter')

    def filter(self, ds):
        """ Filter input datasets <ds> using BaseSearchForm and nameparameters """

        ds = super().filter(ds)
        received_input_text = self.cleaned_data['nameparameters']
        if len(received_input_text) != 0:
            ds = ds.filter(
                parameters__standard_name__icontains=received_input_text)
        return ds
