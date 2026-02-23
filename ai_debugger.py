import os
import google.generativeai as genai
import sys

# Fetching API Key from GitHub Secrets
api_key = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# Using Gemini 1.5 Flash for speed
model = genai.GenerativeModel('gemini-1.5-flash')

# Reading error log passed from the workflow
error_log = sys.argv[1] if len(sys.argv) > 1 else "No error log provided"

prompt = f"""
The following Python code has failed. 
Error Log:
{error_log}

Please provide:
1. Identification of the syntax or logical error.
2. The corrected code block.
3. A brief explanation of the fix.
"""

try:
    response = model.generate_content(prompt)
    print("\n" + "="*40)
    print("🚀 GEMINI AI DEBUGGER REPORT")
    print("="*40)
    print(response.text)
except Exception as e:
    print(f"Error calling Gemini API: {e}")
