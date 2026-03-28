from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

TEXT_MODEL = "llama-3.1-8b-instant"
VISION_MODEL = "llama-3.1-8b-instant"