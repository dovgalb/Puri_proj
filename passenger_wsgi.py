import os, sys
sys.path.insert(0, '/home/b/bogdanfr/bogdanfr.beget.tech/PiriProject')
sys.path.insert(1, '/home/b/bogdanfr/bogdanfr.beget.tech/djangoenv/lib/python3.10/site-packages/django/__init__.py')
os.environ['DJANGO_SETTINGS_MODULE'] = 'PiriProject.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()