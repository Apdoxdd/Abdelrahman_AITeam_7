

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences = [
    "The cat sat on the mat.",
    "A dog is running in the park.",
    "I am learning about embeddings.",
    "The level is just too advanced",
    "The bezel is Tiffany stamped",
    "Don't grip on my hand",
    "I know that I came with a slide from left to right, but now I don't wanna dance",
    "I got too much on the line, too much on my mind, too much ain't enough for my plans",
    "Nike don't pay me to tell you, Just do it They pay me to show you I'll do it again"
]

embeddings = model.encode(sentences)

print("Shape:", embeddings.shape)
print("First 10 values of sentence 0:", embeddings[0][:10])

