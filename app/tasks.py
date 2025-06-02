from datetime import datetime
from .database import SessionLocal
from .models import Task
from celery_worker import celery

@celery.task
def send_reminder_email(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        print(f"[Reminder] Task '{task.title}' is due on {task.due_date}")
        # In production, send real email here.
    db.close()

@celery.task
def send_weekly_summary():
    db = SessionLocal()
    tasks = db.query(Task).filter(Task.is_completed == False).all()
    print("Weekly summary: You have", len(tasks), "pending tasks.")
    # Again, you'd email this summary in production.
    db.close()
