import ollama

response = ollama.embeddings(

	  model = "nomic-embed-text", 
		prompt = "UPI transaction limit is 100000")
embedding = response["embedding"]
print(f"verctor length = {len(embedding)}")
print(f"\n first 10 values:\n")
print(embedding[0:10])