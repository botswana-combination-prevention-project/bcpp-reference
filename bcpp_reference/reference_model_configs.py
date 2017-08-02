from edc_reference import site_reference_configs, ReferenceModelConfig
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

site_reference_configs.register_from_visit_schedule(
    site_visit_schedules=site_visit_schedules)

configs = {
    'bcpp_subject.hivresult': ['hiv_result', 'hiv_result_datetime'],
    'bcpp_subject.hivcareadherence': ['arv_evidence', 'ever_taken_arv', 'on_arv'],
    'bcpp_subject.elisahivresult': ['hiv_result', 'hiv_result_datetime'],
    'bcpp_subject.hivtestinghistory': [
        'verbal_hiv_result', 'other_record', 'has_tested', 'has_record'],
    'bcpp_subject.hivtestreview': ['hiv_test_date', 'recorded_hiv_result'],
    'bcpp_subject.hivresultdocumentation': [
        'result_date', 'result_recorded', 'result_doc_type'],
    'bcpp_subject.circumcision': ['circumcised'],
    'bcpp_subject.hicenrollment': ['hic_permission'],
    'bcpp_subject.sexualbehaviour': ['last_year_partners'],
    'bcpp_subject.subjectvisit': ['survey_schedule', 'survey'],
    'bcpp_subject.immigrationstatus': ['report_datetime']
}
for model, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        model, fields)

reference = ReferenceModelConfig(
    model='bcpp_subject.anonymousconsent', fields=['consent_datetime'])
site_reference_configs.register(reference)
