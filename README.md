# 🧠 TaskMaster Pro – Smart Task & Time Manager

A productivity-focused task management system that helps you organize tasks, schedule reminders, and receive daily/weekly summaries via email. Built with modern Python tooling using FastAPI, Celery, PostgreSQL, Redis, and Docker.

---

## 🚀 Features

- ✅ Create, update, delete, and list tasks via RESTful API
- ⏰ Schedule tasks with due dates and priority
- 📬 Email reminders and weekly productivity summaries
- ⚙️ Background job processing with Celery + Redis
- 🐳 Fully containerized with Docker
- 🗃️ PostgreSQL for persistent storage
- 🔁 Auto-scheduled jobs via Celery Beat

---

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Task Queue**: Celery + Redis
- **Scheduling**: Celery Beat
- **Containerization**: Docker, Docker Compose
- **Email Alerts**: SMTP via Gmail (optional)

---

## 📂 Project Structure

```
├── app/
│ ├── main.py # FastAPI app & routes
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── database.py # DB connection
│ ├── crud.py # DB logic
│ └── tasks.py # Celery background tasks
├── celery_worker.py # Celery app setup & beat config
├── Dockerfile # Image definition
├── docker-compose.yml # Container orchestration
├── requirements.txt
└── .env # Environment variables
```

## 📬 Example Endpoints

# Create Task
```
POST /tasks/
{
  "title": "Finish Resume",
  "description": "Update resume for job application",
  "due_date": "2025-06-03T10:00:00",
  "priority": "High"
}
```

# Trigger Email Summary (manually)
```
POST /send-summary/
```

## 🧪 To-Do / Coming Soon
 JWT-based user authentication

 Web dashboard with Streamlit or React

 Export tasks as PDF/CSV

 Tagging and filters
