import os
import sys
from groq import Groq

# Initialize Groq Client
client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

# Catching the error message from GitHub Actions
error_log = sys.argv[1] if len(sys.argv) > 1 else "No error log provided"

prompt = f"""
Fix the following Python code error and return ONLY the corrected code. 
Do not include any explanations, comments, or backticks.
Error: {error_log}
"""

try:
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    corrected_code = completion.choices[0].message.content.strip()

    # Original file ko update karna
    with open("code_with_error.py", "w") as f:
        f.write(corrected_code)
    
    print("✅ AI has prepared the fix.")

except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
