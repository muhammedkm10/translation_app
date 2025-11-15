# AI_NOTE_TRANSLATOR

## Project Overview
AI_NOTE_TRANSLATOR is a Django-based web application for managing notes, translating them into multiple languages, and viewing translation statistics. JWT-based authentication secures API access.

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






