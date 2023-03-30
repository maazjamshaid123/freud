import streamlit as st
from freud import CustomChatGPT

st.set_page_config(page_title = 'Freud',layout="wide",page_icon="Freud.png", menu_items={
        'Get Help': 'https://www.linkedin.com/in/maazjamshaid/',
        'Report a bug': "https://www.linkedin.com/in/maazjamshaid/",
        'About': '''$Freud$ by [Maaz Jamshaid](https://www.linkedin.com/in/maazjamshaid/), maaz@astroalgo.com'''
    })

st.markdown("---")

col1, col2, col3 = st.columns(3)
with col2:
    st.image('Freud.png')

st.text("by [Maaz Jamshaid](https://www.linkedin.com/in/maazjamshaid/)")

st.markdown("---")

user_input = st.text_input("Give me a detailed description about your dream: ")

if st.button("Ask Freud"):
    response = CustomChatGPT(user_input)
    st.text_area("Patient:", value=response, height=200, max_chars=None, key=None)
