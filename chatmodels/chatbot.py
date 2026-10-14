from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.7
)

messages = []

while True:
    print("----Welcome type 0 to exit----")
    prompt = input("You:")
    messages.append( prompt)

    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append( response.content)
    print("Bot:", response.content)
    