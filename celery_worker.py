from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")

celery = Celery(
    "taskmaster",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BROKER_URL,
)

celery.conf.imports = ("app.tasks",)
celery.conf.beat_schedule = {
    "send-weekly-summary": {
        "task": "app.tasks.send_weekly_summary",
        "schedule": 60.0 * 60 * 24 * 7,  # every 7 days (can change to crontab)
    },
}
celery.conf.timezone = "UTC"
