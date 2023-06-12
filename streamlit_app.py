import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
from PIL import Image

# Ensure your Streamlit secrets are set up with your OpenAI keys
openai.api_key = st.secrets["API_key"]
openai.api_base = st.secrets["API_base"]

# Initiate global history
history = []

def append_history(history, item):
    """
    Function to append an item to the history.
    """
    try:
        history.append(item)
        return history
    except Exception as e:
        st.error(f"Error when appending to history: {e}")
        return history

def get_reply(input_string):
    """
    Function to get a reply using the GPT model from OpenAI.
    """
    try:
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            max_tokens = 1000,
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_string}
            ]
        )
        answer = response["choices"][0]["message"]["content"]
        return answer
    except Exception as e:
        st.error(f"Error when getting reply: {e}")
        return None

def app():
    """
    Main app function.
    """
    try:
        # Set the page configuration
        st.set_page_config(page_title="AuggieGPT", page_icon="agustinjereza.png", layout="wide")

        # Display an image
        img = Image.open("agustinjereza.png")
        new_size = (150, 150)
        img = img.resize(new_size)
        st.image(img)

        # Display the chatbot information
        st.markdown("# Hello, I'm Auggie! How can I assist you today?")
        st.markdown("## Auggie is a ChatGPT-powered chatbot assistant")
        st.markdown("This chatbot assistant is capable of providing answers to questions specifically about the **University of Southern Philippines Foundation (USPF)**.")

        # Collect user input
        user_input = st.text_area("Input your question:", height=5)

        # Process the input and display the response when the 'Submit' button is pressed
        if st.button("Submit"):
            history = append_history(history, ("You: " + user_input))
            output = get_reply(user_input)
            if output is not None:
                history = append_history(history, ("Auggie: " + output))
                for item in history:
                    st.write(item)

        # Display additional information
        st.markdown("-----------\n\nThis project of [Dan Chavez](https://www.dnachavez.ph) leverages the capabilities of generative AI with specific knowledge on a set of topics. Similar to ChatGPT, it can engage the user in a human-like conversation. Through the use of prompt engineering, the AI has been trained with specific information beyond the general knowledge base of ChatGPT.")
        st.markdown("\n\n\nCopyright © 2023 University of Southern Philippines Foundation")
        st.markdown("\n\n\n**Disclaimer:** Auggie may produce inaccurate information about people, places, or facts, especially if the question is outside the scope of topics it was trained on.")
        st.markdown("*Created with ❤️ from Cebu City, Philippines*")

    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    app()
