import streamlit as st
from freud import CustomChatGPT

st.set_page_config(page_title = 'Freud',layout="wide",page_icon="Freud.png")

st.markdown("---")

col1, col2, col3 = st.columns(3)
with col2:
    st.image('Freud.png')

st.markdown("---")

user_input = st.text_input("Give me a detailed description about your dream: ")

if st.button("Ask Freud"):
    response = CustomChatGPT(user_input)
    st.text_area("Patient:", value=response, height=200, max_chars=None, key=None)