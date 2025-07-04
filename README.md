﻿# Django-project
# Internship Project: Django, Celery, Redis, and Telegram Bot Integration

This project was developed as part of an AI internship assignment. It demonstrates the integration of Django-based REST APIs with background task processing using Celery and Redis, as well as Telegram bot interaction for real-time user registration. The application is modular, secure, and follows best practices for environment variable management and asynchronous task execution.

## Features

- JWT-secured authentication and protected routes
- Background email sending using Celery and Redis
- Telegram bot integration using `python-telegram-bot`
- Environment variable handling using `python-decouple`
- Modular Django app structure

## Technologies Used

- Python 3.13
- Django 5.2.3
- Django REST Framework
- Celery 5.5.3
- Redis 5.0+
- python-telegram-bot
- SimpleJWT for JWT authentication
- python-decouple

## Project Structure

myproject/
├── core/ # Public and protected API views
├── users/ # Celery task for email handling
├── telegrambot/ # Telegram bot and user model
├── myproject/ # Django settings and URLs
├── .env.example # Sample environment variable file
├── requirements.txt # Python dependencies
├── manage.py # Django entrypoint
└── README.md # Project documentation


