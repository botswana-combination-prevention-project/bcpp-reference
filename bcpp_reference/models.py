from django.conf import settings
if settings.APP_NAME == 'bcpp_reference':
    from .tests.models import *
