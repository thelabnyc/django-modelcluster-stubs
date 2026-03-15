"""Wrapper to run stubtest with Django properly initialized."""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.mypy_test_settings")

import django

django.setup()

from mypy.stubtest import main  # noqa: E402

sys.exit(main())
