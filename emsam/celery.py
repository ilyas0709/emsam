import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mess.settings")
app = Celery("sushi")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
