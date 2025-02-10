import groq
import pyttsx3
from config import GROQ_API_KEY  # Ensure API key is correctly loaded

# Global Text-to-Speech (TTS) Engine
engine = None  
ENABLE_VOICE = False  # Set to True to enable AI speech, False to disable

def ask_groq(prompt):
    """Sends a prompt to Groq API and returns a response."""
    try:
        client = groq.Client(api_key=GROQ_API_KEY)  # Use the imported key

        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Example Groq model
            messages=[{"role": "user", "content": prompt}],
        )

        response_text = response.choices[0].message.content  # Get response

        # Speak only if voice is enabled
        if ENABLE_VOICE:
            speak(response_text)

        return response_text  # Return response text

    except Exception as e:
        print(f"❌ Error communicating with Groq API: {e}")
        return "⚠️ AI is currently unavailable. Please try again later."

def speak(text):
    """Convert text to speech while avoiding memory leaks."""
    global engine
    if engine is None:
        engine = pyttsx3.init()  # Initialize only once

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"❌ Error in TTS engine: {e}")
