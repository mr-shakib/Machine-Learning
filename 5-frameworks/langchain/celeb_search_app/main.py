import os
import streamlit as st
from constants import gemini_api
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

# Set Gemini API key
os.environ["GOOGLE_API_KEY"] = gemini_api

# Streamlit UI
st.title("LangChain with Google Gemini")
input_text = st.text_input("Enter your text here")

# --- First Prompt ---
first_prompt = PromptTemplate(
    input_variables=["name"],
    template="Tell me about celebrity {name}."
)

# --- Second Prompt ---
second_prompt = PromptTemplate(
    input_variables=["bio"],
    template="Summarize this biography in 3 short sentences: {bio}."
)

# --- Third Prompt ---
third_prompt = PromptTemplate(
    input_variables=["summary"],
    template="List 3 interesting facts from this summary: {summary}."
)

# --- Memory ---
memory = ConversationBufferMemory(input_key="name", memory_key="chat_history")
bio_memory = ConversationBufferMemory(input_key="bio", memory_key="bio_history")
summary_memory = ConversationBufferMemory(input_key="summary", memory_key="summary_history")

# --- Initialize Gemini LLM ---
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
# --- Chain 1: Generate bio ---
chain1 = LLMChain(llm = llm, prompt=first_prompt, output_key="bio", memory=memory)

# --- Chain 2: Summarize bio ---
chain2 = LLMChain(llm=llm, prompt=second_prompt, output_key="summary", memory=bio_memory)

# --- Chain 3: Generate facts ---
chain3 = LLMChain(llm=llm, prompt=third_prompt, output_key="facts", memory=summary_memory)


# --- Combined Runnable Sequence ---
# The output of chain1 feeds into chain2 automatically
full_chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=["name"],
    output_variables=["bio","summary","facts"],
    verbose=True
)


# Generate response
if input_text:
    try:
        result = full_chain({"name": input_text})
        # result is a message object
        st.write(result)

        with st.expander("Bio Generation History"):
            st.info(memory.buffer)
            
        with st.expander("Summary Generation History"):
            st.info(bio_memory.buffer)

        with st.expander("Facts Generation History"):
            st.info(summary_memory.buffer)
            
    except Exception as e:
        st.error(f"Error generating response: {e}")
