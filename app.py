import streamlit as st
from models import generate_content

st.set_page_config(page_title="Gemini Chat")

st.title("Gemini LLM App")

user_input = st.text_area(
    "Enter your prompt",
    placeholder="Ask anything..."
)

if st.button("Search"):
    if not user_input.strip():
        st.error("Please enter a prompt.")
    else:
        try:
            with st.spinner("Thinking..."):
                answer = generate_content(user_input)

            st.success("Response Generated!")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")