import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-8b-8192")  # Default model
ENABLE_VOICE = os.getenv("ENABLE_VOICE", "False").lower() == "true"  # Convert to bool
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# Database Config (if needed later)
DB_URI = os.getenv("DB_URI")

# Ensure critical environment variables exist
if not GROQ_API_KEY:
    raise ValueError("❌ ERROR: GROQ_API_KEY is not set. Please check .env file or environment variables.")

if DEBUG_MODE:
    print(f"🛠 Debug Mode: Enabled\n🤖 Using Model: {GROQ_MODEL}\n🗣 Voice Output: {'Enabled' if ENABLE_VOICE else 'Disabled'}")
