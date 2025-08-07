

import os
import openai
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"

openai.api_key = GROQ_API_KEY
openai.api_base = "https://api.groq.com/openai/v1"

def build_ranking_prompt(jd_text, resumes):
    """
    Build a prompt to rank resumes against the job description.
    """
    resume_blocks = ""
    for i, res in enumerate(resumes, start=1):
        resume_blocks += f"\n\nCandidate {i}:\nFilename: {res['filename']}\nResume:\n{res['content'][:2000]}"

    prompt = f"""
You are an expert technical recruiter.

Here is a Job Description:
{jd_text}

Here are 10 candidate resumes:
{resume_blocks}

🔍 TASK:
Rank the **top 3 most suitable candidates** for this job.
For each one, include:
- Candidate number
- Filename
- Reason why this resume fits best

🎯 Output Format:
1. Candidate X - Filename: XYZ.pdf - Reason
2. Candidate Y - Filename: ABC.pdf - Reason
3. Candidate Z - Filename: DEF.pdf - Reason
"""
    return prompt.strip()

def call_groq_llm(prompt):
    """
    Calls Groq-hosted Mixtral LLM with the given prompt.
    """
    try:
        response = openai.ChatCompletion.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful, smart AI recruiter."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] Groq LLM call failed: {e}")
        return ""
