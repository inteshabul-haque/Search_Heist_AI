import os
import google.generativeai as genai
from dotenv import load_dotenv

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

# ==========================================
# gemini CONFIG
# ==========================================

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ==========================================
# MODEL
# ==========================================

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# ==========================================
# ASK gemini
# ==========================================

def ask_gemini(prompt, dataframe=None):

    try:

        # ==================================
        # DATA CONTEXT
        # ==================================

        dataset_context = ""

        if dataframe is not None:

            dataset_context = f"""

            Dataset Columns:
            {list(dataframe.columns)}

            First 5 Rows:
            {dataframe.head().to_string()}

            """

        # ==================================
        # FINAL PROMPT
        # ==================================

        final_prompt = f"""

        You are Search Heist AI,
        an elite AI marketing intelligence assistant.

        Your job:
        - Analyze campaign data
        - Detect ROAS decline
        - Identify inefficient spend
        - Detect weak-performing campaigns
        - Generate business insights
        - Recommend optimization opportunities
        - Explain findings professionally
        - Keep answers concise and readable

        IMPORTANT:
        - NEVER return HTML
        - NEVER return CSS
        - NEVER return </div>
        - NEVER return code unless asked
        - Return clean readable text only

        USER QUESTION:
        {prompt}

        DATASET:
        {dataset_context}

        """

        # ==================================
        # gemini RESPONSE
        # ==================================

        response = model.generate_content(
            final_prompt
        )

        # ==================================
        # CLEAN RESPONSE
        # ==================================

        final_response = str(response.text)

        # REMOVE BAD HTML
        bad_words = [
            "```",
            "</div>",
            "<div>",
            "/div",
            "html",
            "json"
        ]

        for word in bad_words:

            final_response = final_response.replace(
                word,
                ""
            )

        final_response = final_response.strip()

        # ==================================
        # RETURN
        # ==================================

        return {
            "response": final_response
        }

    except Exception as e:

        return {
            "response": f"""
🎭 The Professor encountered an issue.

{str(e)}
"""
        }