#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

_curdir = os.path.abspath(os.path.dirname(__file__))
_newdir = os.path.abspath(os.path.join(_curdir, "../../../"))
sys.path.remove(_curdir)
sys.path.insert(0, _newdir)


def main():
    """Run administrative tasks."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "src.adapters.django.config.settings"
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
