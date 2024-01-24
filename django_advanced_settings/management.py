from .loader import load_settings

load_settings()

from django.core.management import execute_from_command_line, call_command  # noqa
