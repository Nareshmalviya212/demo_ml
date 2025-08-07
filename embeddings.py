

import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

def load_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Loads HuggingFace sentence transformer model using HF token.
    """
    try:
        model = SentenceTransformer(model_name, use_auth_token=HF_TOKEN)
        return model
    except Exception as e:
        print(f"[ERROR] Failed to load HuggingFace model: {e}")
        return None

def get_embedding(model, text):
    """
    Returns embedding vector for the given text using the model.
    """
    return model.encode(text, convert_to_tensor=True)
