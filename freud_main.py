import streamlit as st
import pyttsx3
import os
from freud import CustomChatGPT

st.set_page_config(page_title='Freud', layout="wide", page_icon="Freud.png", menu_items={
        'Get Help': 'https://www.linkedin.com/in/maazjamshaid/',
        'Report a bug': "https://www.linkedin.com/in/maazjamshaid/",
        'About': '''$Freud$ by [Maaz Jamshaid](https://www.linkedin.com/in/maazjamshaid/), maaz@astroalgo.com'''
    })

st.markdown("---")

col1, col2, col3 = st.columns(3)
with col2:
    st.image('Freud.png')

st.markdown("---")

user_input = st.text_input("Give me a detailed description about your dream: ")

if st.button("Ask Freud"):
    response = CustomChatGPT(user_input)
    st.text_area("Patient:", value=response, height=200, max_chars=None, key=None)

    # Set the LD_LIBRARY_PATH variable to the directory containing the libespeak.so.1 file
    espeak_path = "/usr/lib/x86_64-linux-gnu"
    os.environ["LD_LIBRARY_PATH"] = espeak_path

    # Initialize pyttsx3 TTS engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speech rate (default is 200)
    engine.say(response)
    engine.runAndWait()
