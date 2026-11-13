import math
from ollama import embed

MODEL = "nomic-embed-text"

def cosine_similarity(a, b):
    # Measure similarity between two vectors
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    return dot / (norm_a * norm_b)

def predict(anchor, text_a, text_b):
    # Convert all three stories into embeddings
    response = embed(
        model=MODEL,
        input=[anchor, text_a, text_b],
        truncate=False
    )

    anchor_vec, a_vec, b_vec = response.embeddings

    # Compare each candidate against the anchor
    similarity_a = cosine_similarity(anchor_vec, a_vec)
    similarity_b = cosine_similarity(anchor_vec, b_vec)

    return similarity_a > similarity_b
