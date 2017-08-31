from django.db import models
from django.db.models.deletion import PROTECT

from edc_appointment.models import Appointment
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_mixins.list_model_mixin import ListModelMixin
from edc_base.utils import get_utcnow
from edc_reference.model_mixins import ReferenceModelMixin
from edc_locator.model_mixins import LocatorModelMixin
from edc_constants.constants import YES, POS, NO, NEG


class SubjectVisit(ReferenceModelMixin, BaseUuidModel):

    appointment = models.ForeignKey(Appointment, null=True)

    subject_identifier = models.CharField(max_length=25)

    report_datetime = models.DateTimeField(default=get_utcnow)

    visit_code = models.CharField(max_length=25, default='T0')

#     household_member = models.ForeignKey(HouseholdMember, null=True)

    survey = models.CharField(max_length=25, default='survey')

    survey_schedule = models.CharField(
        max_length=25, default='survey_schedule')

    class Meta:
        ordering = ['report_datetime']


class SubjectConsent(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    consent_datetime = models.DateTimeField(default=get_utcnow)

    dob = models.DateField(null=True)

    citizen = models.CharField(max_length=25, default=YES)

    legal_marriage = models.CharField(max_length=25, null=True)

    marriage_certificate = models.CharField(max_length=25, null=True)


class SubjectLocator(LocatorModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)


class ListModel(ListModelMixin, BaseUuidModel):
    pass


class CrfModelMixin(models.Model):

    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    report_datetime = models.DateTimeField(null=True)

    @property
    def subject_identifier(self):
        return self.subject_visit.subject_identifier

    @property
    def visit_code(self):
        return self.subject_visit.visit_code

    @property
    def visit(self):
        return self.subject_visit

    class Meta:
        abstract = True


class SubjectRequisition(CrfModelMixin, BaseUuidModel):

    panel_name = models.CharField(max_length=25, default='Microtube')


class Circumcision(CrfModelMixin, BaseUuidModel):

    circumcised = models.CharField(max_length=25, default=YES)


class SexualBehaviour(CrfModelMixin, BaseUuidModel):

    ever_sex = models.CharField(max_length=25, default=YES)


class HivResult(ReferenceModelMixin, CrfModelMixin, BaseUuidModel):

    hiv_result = models.CharField(max_length=25, default=POS)

    hiv_result_datetime = models.DateTimeField(default=get_utcnow)


class HivtestReview(ReferenceModelMixin, CrfModelMixin, BaseUuidModel):

    recorded_hiv_result = models.CharField(max_length=25, default=POS)

    hiv_test_date = models.DateTimeField(default=get_utcnow)


class ElisaHivResult(ReferenceModelMixin, CrfModelMixin, BaseUuidModel):

    hiv_result = models.CharField(max_length=25, default=POS)

    hiv_result_datetime = models.DateTimeField(default=get_utcnow)


class HivCareAdherence(CrfModelMixin, BaseUuidModel):

    arv_evidence = models.CharField(max_length=25, default=YES)
    ever_taken_arv = models.CharField(max_length=25, default=YES)
    on_arv = models.CharField(max_length=25, default=YES)


class HivTestingHistory(CrfModelMixin, BaseUuidModel):

    verbal_hiv_result = models.CharField(max_length=25, default=POS)
    other_record = models.CharField(max_length=25, default=NO)
    has_tested = models.CharField(max_length=25, default=YES)
    has_record = models.CharField(max_length=25, default=YES)


class HivResultDocumentation(CrfModelMixin, BaseUuidModel):

    result_date = models.DateField(default=get_utcnow)
    result_recorded = models.CharField(max_length=25, default=POS)
    result_doc_type = models.CharField(max_length=25, default=YES)


class HicEnrollment(CrfModelMixin, BaseUuidModel):

    hiv_result = models.CharField(max_length=25, default=NEG)

    permanent_resident = models.CharField(max_length=25, default=YES)

    intend_residency = models.CharField(max_length=25, default=NO)

    def __str__(self):
        return (f'{self.subject_visit.subject_identifier} '
                f'{self.subject_visit.report_datetime} {self.subject_visit.visit_code}')
