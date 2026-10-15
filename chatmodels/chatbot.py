from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.7
)

print("Choose your Ai mode")
print("press 1 for funny mode")
print("press 2 for Angry mode")
print("3 for sad mode")

choice = int(input("tell your response --"))

if choice == 1:
    mode = "You are a funny assistant."
elif choice == 2:
    mode = "You are an angry assistant."
elif choice == 3:
    mode = "You are a sad assistant."
else:
    mode = "You are a helpful assistant."

messages = [
    SystemMessage(content=mode),
]

while True:
    print("----Welcome type 0 to exit----")
    prompt = input("You:")
    messages.append(HumanMessage(content=prompt))

    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot:", response.content)
    