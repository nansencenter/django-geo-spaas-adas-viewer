from django.test import Client, TestCase
from django.utils import timezone

from geospaas.base_viewer.tests import BaseViewerHTMLParser
from geospaas.catalog.models import Dataset
from geospaas.vocabularies.models import Parameter
from geospaas_adas_viewer.views import AdasIndexView


class GuiIntegrationTests(TestCase):
    '''Integration tests for GET and POST methods of GUI'''
    fixtures = ["vocabularies", "catalog"]

    def setUp(self):
        self.client = Client()
        # this BaseViewerHTMLParser is configured to store the desired data of td tag into self.data
        self.parser = BaseViewerHTMLParser()

    def test_the_post_verb_of_GUI_with_unique_part_of_parameter_name(self):
        """shall return the uri of fixtures' datasets in the specified placement
        of datasets inside the resulted HTML in the case of a POST with a part of
        parameter name inside the charfield of parameter in form """
        res3 = self.client.post('/adas/', {
            'time_coverage_start': timezone.datetime(2000, 12, 29),
            'time_coverage_end': timezone.datetime(2020, 1, 1),
            'source': 1,
            'nameparameters': 'from_direction'})  # <= Notice the part of the name 'wind_from_direction' provided by user
        self.assertEqual(res3.status_code, 200)
        self.parser.feed(str(res3.content))
        # both datasets must be in the html
        self.assertFalse(any([('file://localhost/some/test/file1.ext' in dat)
                             for dat in self.parser.data]))
        # The second one should not be in the html
        self.assertTrue(any([('file://localhost/some/test/file2.ext' in dat)
                              for dat in self.parser.data]))

    def test_post_with_common_part_of_parameter_name(self):
        """shall return the uri of fixtures' datasets in the specified placement
        of datasets inside the resulted HTML in the case of a POST request without
        any polygon from user """
        res4 = self.client.post('/adas/', {
            'time_coverage_start': timezone.datetime(2000, 12, 29),
            'time_coverage_end': timezone.datetime(2020, 1, 1),
            'source': 1,
            'nameparameters': 'wind'})  # <= Notice the part of both names of 'wind_speed' and 'wind_from_direction' provided by user
        self.assertEqual(res4.status_code, 200)
        self.parser.feed(str(res4.content))
        # both datasets must be in the html
        self.assertTrue(any([('file://localhost/some/test/file1.ext' in dat)
                             for dat in self.parser.data]))
        self.assertTrue(any([('file://localhost/some/test/file2.ext' in dat)
                             for dat in self.parser.data]))

    def test_the_get(self):
        """shall return ALL uri of fixtures' datasets in the specified placement
        of datasets inside the resulted HTML in the case of a GET request"""
        res5 = self.client.get('/adas/')
        self.assertEqual(res5.status_code, 200)
        self.parser.feed(str(res5.content))
        # both datasets must be in the html
        self.assertTrue(any([('file://localhost/some/test/file1.ext' in dat)
                             for dat in self.parser.data]))
        self.assertTrue(any([('file://localhost/some/test/file2.ext' in dat)
                             for dat in self.parser.data]))


class ADASSearchFormTests(TestCase):
    """ Unit tests for filter method which is placed inside the basic form """
    fixtures = ["vocabularies", "catalog"]

    def test_filtering_functionality_by_a_unique_part_of_parameter_name(self):
        """shall return the first dataset in fixtures
        since the 'from_direction' is a portion of name of parameters for
        the tjuetusen dataset """
        form = AdasIndexView.form_class({'polygon': '',
                                              'time_coverage_start': timezone.datetime(2000, 12, 29),
                                              'time_coverage_end': timezone.datetime(2020, 1, 1),
                                              'source': 1,
                                              'nameparameters': 'from_direction'})  # <= Notice the difference betweem tests####
        form.is_valid()
        ds = Dataset.objects.all()
        ds = form.filter(ds)
        # one of the datasets should remain as the result of filtering with dummy parameter
        self.assertEqual(len(ds), 1)
        self.assertEqual(ds.first().entry_id,
                         'NERSC_test_dataset_tjuetusen')

    def test_filter_with_common_part_of_parameter_name(self):
        """ Shall return both fixture datasets since both of them have 'ind_' in their parameters' name """
        form = AdasIndexView.form_class({'polygon': '',
                                              'time_coverage_start': timezone.datetime(2000, 12, 29),
                                              'time_coverage_end': timezone.datetime(2020, 1, 1),
                                              'source': 1,
                                              'nameparameters': 'ind_'})  # <= Notice the difference betweem tests####
        form.is_valid()
        ds = Dataset.objects.all()
        ds = form.filter(ds)
        # Both datasets should remain as the result of filtering
        self.assertEqual(len(ds), 2)

    def test_filter_with_meaningless_parameter_name(self):
        """ Shall return no fixture datasets since none of them have 'iiii' in their parameters' name """
        form = AdasIndexView.form_class({'polygon': '',
                                              'time_coverage_start': timezone.datetime(2000, 12, 29),
                                              'time_coverage_end': timezone.datetime(2020, 1, 1),
                                              'source': 1,
                                              'nameparameters': 'iiii'})  # <= Notice the difference betweem tests####
        form.is_valid()
        ds = Dataset.objects.all()
        ds = form.filter(ds)
        # No datasets should remain as the result of filtering
        self.assertEqual(len(ds), 0)
