import os
import sys

path = '/home/pinkey0630/my-first-blog'  # use your own username here
if path not in sys.path:
        sys.path.append(path)

        os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
