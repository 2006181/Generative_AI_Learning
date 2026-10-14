from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import dotenv_values


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    encode_kwargs={"normalize_embeddings": True},
)

query_result = embeddings.embed_query("This is a test document.")
print("Query embedding:", query_result)