

from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

sentences = [
    "The cat sat on the mat.",
    "A dog is running in the park.",
"I am learning about embeddings.",
    "I can't be pale in my casket",                         
    "Make sure I die with a tan, it's part of the brand",                      
    "I know that I came with a slide from left to right, but now I don't wanna dance",             
    "Cannot depend on the man I slide her some bread in a jam, that's just who I am",  
    "Customs just wavin' at us from the window They don't even come on the plane when we land",              
    "Anyone else would retire, but I'm not content",                   
    "I wanna bury these niggas like twenty feet down so no one can find them again",           
]

embeddings = model.encode(sentences)

pairs = [(0, 1), (2, 3), (0, 4), (5, 6)]

for i, j in pairs:
    score = cosine_similarity(embeddings[i], embeddings[j])
    print(f"{score:.3f} | sentence {i} vs sentence {j}")

