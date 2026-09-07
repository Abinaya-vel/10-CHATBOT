# 10 AI Chatbots - Deployment Guide

Included projects:
1. JobGenie AI
2. Healora AI
3. FoodBuddy AI
4. CodeGuru AI
5. StyleMuse AI
6. StudyMate AI
7. TravelMate AI
8. FinanceWise AI
9. BizBuddy AI
10. EcoGuide AI

Each project is independent and ready for local Flask testing and Render deployment.

## Common setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your Gemini API key.

## Run

```bash
python app.py
```

## GitHub + Render

For each chatbot:
1. Create a separate GitHub repository.
2. Upload the chatbot folder contents.
3. In Render, create a Web Service and connect the repository.
4. Build Command:
   `pip install -r requirements.txt`
5. Start Command:
   `gunicorn app:app`
6. Add `GEMINI_API_KEY` and `GEMINI_MODEL` as Render environment variables.
7. Deploy.

The `gunicorn` dependency is already included in every `requirements.txt`, avoiding the common `gunicorn: command not found` deployment error.
