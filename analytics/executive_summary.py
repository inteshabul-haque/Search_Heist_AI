import os
import google.generativeai as genai

from dotenv import load_dotenv

# ============================================
# LOAD ENV
# ============================================

load_dotenv()

# ============================================
# gemini CONFIG
# ============================================

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ============================================
# MODEL
# ============================================

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# ============================================
# EXECUTIVE SUMMARY
# ============================================

def generate_executive_summary(
    df,
    user_query,
    kpi_results,
    campaign_results
):

    prompt = f"""

You are Search Heist AI.

You are an AI-powered
marketing intelligence copilot.

USER QUESTION:
{user_query}

KPI RESULTS:
{kpi_results}

CAMPAIGN RESULTS:
{campaign_results}

DATASET COLUMNS:
{df.columns.tolist()}

TOP DATA:
{df.head(10).to_string(index=False)}

Generate:
- executive summary
- business insights
- risks
- optimization opportunities
- recommendations

"""

    response = model.generate_content(
        prompt
    )

    return response.text