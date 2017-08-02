# from edc_reference.site import site_reference_configs
# from pprint import pprint
from bcpp_reference.tests.models import HivResult, SubjectVisit
from django.test import TestCase, tag
from edc_constants.constants import POS
from edc_reference.models import Reference
from edc_reference.tests import ReferenceTestHelper

from .reference_config_helper import ReferenceConfigHelper
from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow
from pprint import pprint


class TestReference(TestCase):

    reference_config_helper = ReferenceConfigHelper()
    reference_helper_cls = ReferenceTestHelper

    def setUp(self):
        self.subject_identifier = '12345'
        self.reference_config_helper.reconfigure('bcpp_reference')
        self.reference_helper = self.reference_helper_cls(
            visit_model='bcpp_reference.subjectvisit',
            subject_identifier=self.subject_identifier)
        self.subject_visit = SubjectVisit.objects.create(
            subject_identifier=self.subject_identifier,
            visit_code='T0',
            survey_schedule='survey_schedule',
            survey='survey')

#     def test_(self):
#         pprint(site_reference_configs.registry)

    def test_subject_visit(self):
        values = []
        for obj in Reference.objects.filter(model='bcpp_reference.subjectvisit'):
            values.append(obj.value)
        self.assertIn(self.subject_visit.report_datetime, values)
        self.assertIn(self.subject_visit.survey_schedule, values)
        self.assertIn(self.subject_visit.survey, values)

    def test_hiv_result(self):
        model_obj = HivResult.objects.create(
            subject_visit=self.subject_visit,
            hiv_result_datetime=get_utcnow() - relativedelta(years=1))
        values = {}
        for obj in Reference.objects.filter(model='bcpp_reference.hivresult'):
            values.update({obj.field_name: obj.value})
        self.assertEqual(POS, values.get('hiv_result'))
        self.assertEqual(model_obj.hiv_result_datetime,
                         values.get('hiv_result_datetime'))
        self.assertEqual(model_obj.subject_visit.report_datetime,
                         values.get('report_datetime'))
