"""
WSGI config for blissbowl project.

It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blissbowl.settings')

# WSGI application callable
application = get_wsgi_application()

# Expose the WSGI callable as `app` for Vercel
app = application
