# EcoGuide AI

Sustainability and environmental assistant

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Add your Gemini API key to `.env`.
4. Run:
   `python app.py`
5. Open `http://127.0.0.1:5000`

## Render deployment

- Push this folder to its own GitHub repository.
- Create a Render Web Service from that repository.
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Add environment variables:
  - `GEMINI_API_KEY` = your real key
  - `GEMINI_MODEL` = `gemini-2.5-flash`

Never commit `.env` or your API key.
