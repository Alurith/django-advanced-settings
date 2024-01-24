import os
from django.conf import ENVIRONMENT_VARIABLE as DJANGO_SETTINGS_MODULE
from django.utils.module_loading import import_string
from django.conf import settings


DJANGO_SETTINGS_CLASS = "DJANGO_SETTINGS_CLASS"


def load_settings():
    setting_module = os.environ.get(DJANGO_SETTINGS_MODULE)
    setting_class = os.environ.get(DJANGO_SETTINGS_CLASS, "BaseProjectSettings")

    Setting = import_string(f"{setting_module}.{setting_class}")
    if settings.configured:
        return False
    settings.configure(**Setting().model_dump())
