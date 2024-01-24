# django-advanced-settings
Django settings with Pydantic 2

This package is still in progress and probaly not ready for production. Tested only on python 3.10 and with django 4.2, it will probably work with other versions.


## How to install
`pip install git+https://github.com/Alurith/django-advanced-settings.git`

## How to use
If you use the management command change the manage.py as follow
``` python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
    try:
        # from django.core.management import execute_from_command_line
        from django_advanced_settings.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
```
If you use wsgi import this inside wsgi.py
``` python
from django_advanced_settings.wsgi import get_wsgi_application
```
If you use asgi import this inside asgi.py
```python
from django_advanced_settings.asgi import get_asgi_application
```

In your settings.py you can import *django-advanced-settings* import the default settings.

``` python
from pathlib import Path
from pydantic import DirectoryPath

from django_advanced_settings.settings import DefaultSettings
from django_advanced_settings.schemas import DottedString, DatabaseSchema


class BaseProjectSettings(DefaultSettings):
    BASE_DIR: DirectoryPath = Path(__file__).resolve().parent.parent
    DATABASES: dict[str, DatabaseSchema] = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    WSGI_APPLICATION: DottedString = "project_name.wsgi.application"
    ROOT_URLCONF: DottedString = "project_name.urls"

```
By default *django-advanced-settings* will try to import `BaseProjectSettings`, you can change this beheaviour via the env variable `DJANGO_SETTINGS_CLASS`

## TODOs
- [ ] Fix the missing types
- [ ] Write tests
- [ ] Create a CI to run tests with different python's version
- [ ] Write a migration script to migrate the current settings to a *django-advanced-settings* class
- [ ] Release on PyPi
