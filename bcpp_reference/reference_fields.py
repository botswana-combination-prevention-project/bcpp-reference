from edc_reference.site import site_reference_configs
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

site_reference_configs.register_from_visit_schedule(
    site_visit_schedules=site_visit_schedules)

configs = {
    'bcpp_subject.HivResult': ['hiv_result', 'hiv_result_datetime'],
    'bcpp_subject.HivCareAdherence': [
        'arv_evidence', 'ever_taken_arv', 'arv_evidence', 'on_arv'],
    'bcpp_subject.ElisaHivResult': ['hiv_result', 'hiv_result_datetime'],
    'bcpp_subject.hivtestinghistory': [
        'verbal_hiv_result', 'other_record', 'has_tested'],
    'bcpp_subject.hivtestreview': ['hiv_test_date', 'recorded_hiv_result'],
    'bcpp_subject.hivresultdocumentation': [
        'result_date', 'result_recorded', 'result_doc_type'],
    'bcpp_subject.circumcision': ['circumcised'],
    'bcpp_subject.hicenrollment': ['hic_permission'],
}
for model, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        model, fields)
