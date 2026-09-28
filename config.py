import os
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "ollama")
MODEL = os.getenv("MODEL", "qwen2.5:1.5b")

if PROVIDER == "ollama":
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
elif PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
else:
    BASE_URL = None
    API_KEY = os.getenv("OPENAI_API_KEY")

COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000,
}

QUESTIONS = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Is DS303 more expensive than CS101, and by how much?",
    "Give me a two-line welcome message for a new student."
]