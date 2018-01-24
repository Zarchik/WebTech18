"""
WSGI config for ask project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

#sys.path.insert(0, '/usr/lib/python3/dist-packages/')
#sys.path.insert(0, '/usr/lib/python3/dist-packages/')
#sys.path.insert(0, '/usr/lib/python3/dist-packages/django/core/')

#os.environ["DJANGO_SETTINGS_MODULE"] = "ask.settings"

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask.settings")

application = get_wsgi_application()
