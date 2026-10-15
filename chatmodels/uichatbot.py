import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

st.set_page_config(page_title="🤖Mood Based AI Chatbot")

st.title("🤖Mood Based AI Chatbot")

# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.7
)

# Choose AI mode
st.subheader("Choose your AI mode")

choice = st.radio(
    "Select a mode:",
    ["Funny Mode", "Angry Mode", "Sad Mode", "Helpful Mode"],
    horizontal=True
)

# Set system role
if choice == "Funny Mode":
    mode = "You are a funny assistant."
elif choice == "Angry Mode":
    mode = "You are an angry assistant."
elif choice == "Sad Mode":
    mode = "You are a sad assistant."
else:
    mode = "You are a helpful assistant."

# Initialize conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Update mode when the user changes their selection
if "current_mode" not in st.session_state:
    st.session_state.current_mode = choice

if st.session_state.current_mode != choice:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]
    st.session_state.current_mode = choice

# Display conversation history
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            content = message.content

            if isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        st.write(item.get("text", ""))
            else:
                st.write(content)

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:
    if prompt == "0":
        st.stop()

    # Display user message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)

            content = response.content

            if isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        st.write(item.get("text", ""))
            else:
                st.write(content)

    # Save AI response
    st.session_state.messages.append(
        AIMessage(content=content)
    )