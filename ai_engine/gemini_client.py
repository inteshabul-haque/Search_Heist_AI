import os

from dotenv import load_dotenv

import google.generativeai as genai

# ============================================================
# LOAD ENV
# ============================================================

load_dotenv()

# ============================================================
# API KEY
# ============================================================

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

# ============================================================
# CONFIG
# ============================================================

genai.configure(
    api_key=API_KEY
)

# ============================================================
# MODEL
# ============================================================

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash"
)

# ============================================================
# ASK GEMINI
# ============================================================

def ask_gemini(prompt):

    try:

        response = model.generate_content(
            prompt
        )

        if response.text:

            return response.text

        return "No response generated."

    except Exception as e:

        return f"Gemini Error: {str(e)}"