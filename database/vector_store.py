import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim=128):
        self.index = faiss.IndexFlatL2(dim)

    def add_mission(self, mission_text):
        """Convert mission text to vector and store in FAISS."""
        vector = np.random.rand(128).astype(np.float32)  # Replace with real embeddings later
        self.index.add(np.array([vector]))
        return vector

    def search_mission(self, query_vector, top_k=3):
        """Search for similar past missions."""
        distances, indices = self.index.search(np.array([query_vector]), top_k)
        return distances, indices
