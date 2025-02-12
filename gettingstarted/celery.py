# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from django.conf import settings

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gettingstarted.settings')

# app = Celery('gettingstarted')
# app.conf.enable_utc = False

# app.conf.update(timezone = 'America/New_York')

# app.config_from_object(settings, namespace='CELERY')

# # Celery Beat Settings

# app.autodiscover_tasks()

# @app.task(blind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
# ==================================================================================== #

import os
from celery import Celery
from decouple import config

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gettingstarted.settings')

app = Celery('gettingstarted')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# We used CELERY_BROKER_URL in settings.py instead of:
# app.conf.broker_url = ''

# We used CELERY_BEAT_SCHEDULER in settings.py instead of:
# app.conf.beat_scheduler = ''django_celery_beat.schedulers.DatabaseScheduler'

# ===============================================================================
# from celery.schedules import crontab

# # Below is for illustration purposes. We 
# # configured so we can adjust scheduling 
# # in the Django admin to manage all 
# # Periodic Tasks like below
# app.conf.beat_schedule = {
#     'multiply-task-crontab': {
#         'task': 'multiply_two_numbers',
#         'schedule': crontab(hour=7, minute=30, day_of_week=1),
#         'args': (16, 16),
#     },
#     'multiply-every-5-seconds': {
#         'task': 'multiply_two_numbers',
#         'schedule': 5.0,
#         'args': (16, 16)
#     },
#     'add-every-30-seconds': {
#         'task': 'movies.tasks.add',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
