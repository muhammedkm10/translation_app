# AI Notes Translator

## Project Overview
AI Notes Translator is a web application built with **Django** (backend) and **React/Flutter** (frontend) that allows users to manage notes, translate them to different languages, and track popularity. It uses **Redis** for caching popular notes and **PostgreSQL** as the primary database.

---

## Tech Stack
- **Backend:** Django 5.2, Django REST Framework
- **Frontend:** React / Flutter (your choice)
- **Database:** PostgreSQL (Neon / Local)
- **Caching:** Redis (Upstash / Local)
- **Authentication:** JWT (via `djangorestframework-simplejwt`)
- **Containerization:** Docker, Docker Compose
- **Hosting:** AWS EC2 (or EKS for Kubernetes)
- **Storage:** AWS S3
- **Others:** Celery + Redis (for async tasks), Gunicorn

---

## Setup Instructions

### **Local Development**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/translation_app.git
   cd translation_app
