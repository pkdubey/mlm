# Celery is optional - only imported when celery is installed
try:
    from config.celery import app as celery_app
    __all__ = ('celery_app',)
except ImportError:
    pass
