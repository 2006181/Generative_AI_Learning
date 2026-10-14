from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tiktoken import model

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.0-flash",
    max_tokens=20,
    temperature=0.7,
    timeout=60
)
try:
     response = model.invoke("Why do parrots talk?")
     print(response.content)

except Exception as e:
     print("Error:", e)
