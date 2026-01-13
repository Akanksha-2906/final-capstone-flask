from celery_app import celery
import time

@celery.task
def long_task():
    time.sleep(5)
    return "Background task completed"
