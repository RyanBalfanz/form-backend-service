# pylint: disable=wildcard-import,unused-wildcard-import
from .settings_base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=True)
