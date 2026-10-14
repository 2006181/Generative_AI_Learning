from dotenv import dotenv_values
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

ENV_PATH = r"C:\Users\Rahul gupta\OneDrive\Documents\GENERATIVE AI.env"

config = dotenv_values(ENV_PATH)
hf_token = config.get("HUGGINGFACEHUB_API_TOKEN")

if not hf_token:
  raise ValueError("Hugging Face token .env file mein nahi mila.")

print("Token loaded:", bool(hf_token))

llm = HuggingFaceEndpoint(
repo_id="deepseek-ai/DeepSeek-R1",
huggingfacehub_api_token=hf_token,
provider="auto",
max_new_tokens=100,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Who are you?")
print(response.content)
 