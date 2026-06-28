from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Did you create a .env file?")
