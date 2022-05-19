import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News_02.settings')

app = Celery('News_02')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'news_every_week': {
        'task': 'newsapp.tasks.weekly_digest',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}
