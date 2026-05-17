try:
    import os
    from celery import Celery
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    app = Celery('mlm_project')
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.autodiscover_tasks()
except ImportError:
    pass
