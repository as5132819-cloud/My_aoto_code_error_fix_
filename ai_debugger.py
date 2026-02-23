import os
import google.generativeai as genai
import sys

# API Key setup
api_key = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# 2026 version fix: Try using 'gemini-1.5-flash-latest' or just 'gemini-1.5-flash'
# Adding safety to the model name
model = genai.GenerativeModel('gemini-1.5-flash')

error_log = sys.argv[1] if len(sys.argv) > 1 else "No error log provided"

prompt = f"""
Identify the error in this Python code and provide a fix.
Error: {error_log}
"""

try:
    # Adding a safety check for the API version
    response = model.generate_content(prompt)
    print("\n🚀 GEMINI AI DEBUGGER REPORT")
    print(response.text)
except Exception as e:
    print(f"Error calling Gemini API: {e}")
