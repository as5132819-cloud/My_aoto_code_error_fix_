import os
import sys
from groq import Groq

# Initialize Groq Client using the Secret Key
client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

# Catching the error message from GitHub Actions
error_log = sys.argv[1] if len(sys.argv) > 1 else "No error log provided"

prompt = f"""
The following Python code failed. 
Error Log: {error_log}

Please:
1. Identify the mistake.
2. Provide the corrected code.
3. Explain why it failed.
"""

try:
    # Fast Inference with Llama 3.3
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    print("\n" + "="*45)
    print("⚡ GROQ AI FAST DEBUGGER REPORT")
    print("="*45)
    print(completion.choices[0].message.content)

except Exception as e:
    print(f"❌ Groq API Error: {e}")
