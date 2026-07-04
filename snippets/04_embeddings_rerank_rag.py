"""04_embeddings_rerank_rag.py — Two-stage retrieve-then-rerank RAG pipeline.

Stage 1: encode query + corpus with a sentence-transformer embedding model,
retrieve top-K by cosine similarity (fast, cheap).

Stage 2: rerank the top-K with a cross-encoder reranker (slow, accurate).
The cross-encoder jointly attends to (query, doc) so it scores relevance
much better than a bi-encoder embedding similarity.

Dependencies:
    pip install sentence-transformers FlagEmbedding

Notes:
    - normalize_embeddings=True is REQUIRED for cosine similarity via dot
      product. Skip it and recall numbers quietly drop.
    - FlagReranker.compute_score accepts a list of [query, doc] pairs.
      Set normalize=True to get scores in [0, 1].
    - For production: swap the in-memory corpus for a vector DB (Qdrant,
      Milvus, pgvector) and only send top-K candidates to the reranker.
"""
from sentence_transformers import SentenceTransformer
from FlagEmbedding import FlagReranker

EMBEDDER_ID = "Alibaba-NLP/gte-modernbert-base"
RERANKER_ID = "BAAI/bge-reranker-v2-m3"

CORPUS = [
    "Paris is the capital of France.",
    "Rome is the capital of Italy.",
    "Berlin is the capital of Germany.",
    "Madrid is the capital of Spain.",
    "Lisbon is the capital of Portugal.",
]
QUERY = "What is the capital of France?"
TOP_K = 3


def main() -> None:
    # Stage 1: dense retrieval
    embedder = SentenceTransformer(EMBEDDER_ID)
    doc_embs = embedder.encode(CORPUS, normalize_embeddings=True)
    q_emb = embedder.encode([QUERY], normalize_embeddings=True)

    # Cosine similarity = dot product of L2-normalized vectors
    scores = (doc_embs @ q_emb.T).ravel()
    top_idx = scores.argsort()[::-1][:TOP_K]
    candidates = [CORPUS[i] for i in top_idx]
    print("Stage 1 (dense retrieval) top candidates:")
    for i, c in zip(top_idx, candidates):
        print(f"  [{scores[i]:.4f}] {c}")

    # Stage 2: cross-encoder rerank
    reranker = FlagReranker(RERANKER_ID, use_fp16=True)
    pairs = [[QUERY, c] for c in candidates]
    rerank_scores = reranker.compute_score(pairs, normalize=True)

    print("\nStage 2 (cross-encoder rerank):")
    for c, s in sorted(zip(candidates, rerank_scores), key=lambda x: -x[1]):
        print(f"  [{s:.4f}] {c}")

    best = sorted(zip(candidates, rerank_scores), key=lambda x: -x[1])[0]
    print(f"\nFinal answer: {best[0]}")


if __name__ == "__main__":
    main()
