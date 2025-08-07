

from embeddings import load_embedding_model, get_embedding
from llm_engine import build_ranking_prompt, call_groq_llm
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_top_resumes_by_embedding(jd_text, resumes, top_n=10):
    """
    Filter top N resumes using cosine similarity on embeddings.
    """
    model = load_embedding_model()
    jd_vector = get_embedding(model, jd_text)
    results = []

    for res in resumes:
        res_vector = get_embedding(model, res['content'])
        score = float(cosine_similarity([jd_vector], [res_vector])[0][0])
        results.append({**res, "embedding_score": score})

    # Sort by similarity
    top_resumes = sorted(results, key=lambda x: x["embedding_score"], reverse=True)[:top_n]
    return top_resumes

def rank_resumes_with_llm(jd_text, resumes, top_n=10):
    """
    Combines embedding filtering + LLM prompt ranking.
    """
    top_resumes = get_top_resumes_by_embedding(jd_text, resumes, top_n=top_n)
    prompt = build_ranking_prompt(jd_text, top_resumes)
    response = call_groq_llm(prompt)
    return response
