# streamlit code

#  conda activate  AI
# file path
# streamlit run app.py
# then it will open in browser 
import streamlit as st
from models import generate_content

st.title('Streamlit Gemini LLM App')
st.subheader('LLM')

user_input = st.text_input(
    'Enter your prompt',
    placeholder='Enter any input'
)

if st.button('Search'):
    if user_input.strip() == '':
        st.error('Write a valid prompt')

    else:
        with st.spinner('Thinking...'):
            answer = generate_content(user_input)

        st.success('Response Generated!')
        st.write(answer)