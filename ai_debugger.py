import os
import sys
from google import genai

# Setup client - it automatically uses the GEMINI_API_KEY env variable
client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

# Getting error log from the workflow arguments
error_log = sys.argv[1] if len(sys.argv) > 1 else "No error log provided"

prompt = f"""
The Python script 'code_with_error.py' failed with the following error:
{error_log}

Please provide:
1. A brief explanation of what went wrong.
2. The complete corrected code.
"""

try:
    # Using Gemini 2.0 Flash (most stable in 2026 for debugging)
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
    print("\n" + "="*40)
    print("🚀 GEMINI AI DEBUGGER REPORT")
    print("="*40)
    print(response.text)
except Exception as e:
    print(f"Failed to get help from Gemini: {e}")
