import os
import celery


class CustomCeleryApp(celery.Celery):
    pass


# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

app = CustomCeleryApp('main')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


class Queues():
    DEFAULT = 'default'
    HEAVY = 'heavy'
    CRONJOB = 'cronjob'

    DEV_QUEUES = (
        DEFAULT,
        HEAVY,
        CRONJOB,
    )


app.conf.task_default_queue = Queues.DEFAULT


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
