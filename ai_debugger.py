import os
import sys
from google import genai

# Setup client (It automatically picks GEMINI_API_KEY from environment)
client = genai.Client()

# Get the error message from GitHub Action arguments
error_log = sys.argv[1] if len(sys.argv) > 1 else "No error log provided"

prompt = f"Identify the error in this code and provide a fix: {error_log}"

try:
    # Using the latest Gemini 3 Flash model
    response = client.models.generate_content(
        model="gemini-2.0-flash", # Or gemini-3-flash-preview if available
        contents=prompt
    )
    print("\n🚀 GEMINI AI DEBUGGER REPORT")
    print(response.text)
except Exception as e:
    print(f"Error calling Gemini API: {e}")
