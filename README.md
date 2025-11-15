# AI_NOTE_TRANSLATOR

## Project Overview
AI_NOTE_TRANSLATOR is a Django-based web application for managing notes, translating them into multiple languages, and viewing translation statistics. JWT-based authentication secures API access.


## Api documentation
link : https://inventory-1173.postman.co/workspace/inventory-Workspace~b0df5fb5-1253-465e-82f6-be6967628eeb/request/35166923-4397f9c1-8590-4e2c-b399-1705332e88ae?action=share&creator=35166923&active-environment=35166923-398c3e2e-419a-46a7-b3e7-668d06c199ac
---

## Tech Stack
- **Backend:** Django 5.2, Django REST Framework
- **Database:** PostgreSQL (local or cloud)
- **Authentication:** JWT (via `djangorestframework-simplejwt`)
- **Containerization:** Docker

---
---

##  Design Decisions
- **PostgreSQL:**  Reliable relational database, works seamlessly with Django ORM
- **JWT:** Stateless authentication suitable for APIs and clients
- **Docker:** Simplifies setup and ensures consistent environment across systems

---

---

##  Known Limitations / Next Steps
- No rate-limiting on translation API
- No user roles implemented yet

---
---

##  Next steps:
- Add unit & integration tests

---

## Design

### High-Level Design (HLD)
LINK : https://app.diagrams.net/#G12jNZMZoT_zO9Oto5s1UyuR270ohUuW6y#%7B%22pageId%22%3A%22FhFMXiOWkhA7z9hHYa80%22%7D

- **Backend**: Django + DRF
- **Database**: PostgreSQL
- **Cache**: Redis
- **Authentication**: JWT
- **Containerization**: Docker

### Low-Level Design (LLD)
LINK : https://app.diagrams.net/#G1qf9q7xcDoRk7rtCmePVWWgT4P1yTrRrD#%7B%22pageId%22%3A%22UtLC6lcEu0-bIKd4OWEP%22%7D

- **Models**:
  - Note: id, title, original_text, original_language
  - Translation: id, note_id, translated_text, translated_language
- **API Endpoints**:
  - `/api/notes/` → CRUD for notes
  - `/api/translate/<note_id>/` → Translate a note
  - `/api/stats/` → Translation stats
  - `/api/popular_notes/` → Popular notes from cache





## Setup Instructions

###  Local Development

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/AI_NOTE_TRANSLATOR.git
cd AI_NOTE_TRANSLATOR


2.Create a virtual environment and activate it:
python -m venv env
source env/bin/activate   # Linux/macOS
env\Scripts\activate      # Windows


3. Install requirments
pip install -r requirements.txt


4. Create a .env file and add environment variables


5.Start the server:
python manage.py runserver

Using Docker

1. Build the image:
docker build -t ai-notes .


2. Run container:
docker compose up


Deploy on AWS
Launch an EC2 instance (Ubuntu)
Install Docker & Docker Compose
Pull your Docker image from Docker Hub or build it on EC2
Run docker compose up -d
Configure security group to allow port 8000 (or 80 if using Nginx)






