text = """
Artificial Intelligence is a field of computer science.
Machine learning allows computers to learn from data.
Deep learning uses neural networks.
Large language models process tokens.
RAG combines retrieval with generation.
"""

words = text.split()

print("Total words:", len(words))

context_limit = 20

context = words[:context_limit]

print("\nContext:")
print(" ".join(context))