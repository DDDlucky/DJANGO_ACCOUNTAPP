import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techpit.settings')

application = get_wsgi_application()

# ========以下をすべて追加========
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
