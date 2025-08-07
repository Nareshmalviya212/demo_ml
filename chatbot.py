

from llm_engine import call_groq_llm

def query_candidates_with_llm(user_query, resumes):
    from llm_engine import call_groq_llm

    resume_blocks = ""
    for i, res in enumerate(resumes, 1):
        resume_blocks += f"\n\nCandidate {i}: {res['filename']}\n{res['content'][:2000]}"

    prompt = f"""
You are a helpful and friendly AI recruiter assistant.

Here is a list of resume data:
{resume_blocks}

A recruiter has asked the following question:
\"\"\"{user_query}\"\"\"

Your job is to:
- Analyze all resumes
- Provide a clear and natural response
- Speak conversationally, like you're talking to a colleague
- If it helps, feel free to use bullet points or short numbered lists
- Mention candidate filenames and why they match
- If no candidates match, say so politely

Keep your answer concise, insightful, and recruiter-friendly.
"""
    return call_groq_llm(prompt)

