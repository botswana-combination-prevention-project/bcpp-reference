from django.test import TestCase, tag

from edc_reference.site import site_reference_configs
from pprint import pprint


class TestReference(TestCase):

    def test_(self):
        pprint(site_reference_configs.registry)
