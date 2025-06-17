# myproject/celery.py

import os
from celery import Celery

# Set default Django settings module for 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # Replace 'myproject' with your project name

# Create a new Celery instance and configure it using Django's settings
app = Celery('myproject')

# Load custom config from Django settings, using CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover all tasks.py files in installed apps
app.autodiscover_tasks()

# Optional: Print task loading info for debug
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
