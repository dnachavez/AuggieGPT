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
global history

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
                {"role": "user", "content": "What is USPF?"},
                {"role": "assistant", "content": "The University of Southern Philippines Foundation (USPF), founded in 1927 as the Southern Institute, is a private, non-sectarian educational institution that offers a wide range of programs in various fields of study, including arts and sciences, business management and accountancy, computer studies, engineering and architecture, education, and health sciences. The university has been in operation for over 90 years as an academic institution and has served the nation by producing professionals in different fields of specialization. It gained university status in 1949 and was renamed the University of the Southern Philippines. In 1959, it became a non-stock, non-profit foundation. The university's main campus is located in Lahug, Cebu City."},
                {"role": "user", "content": "What is the history of USPF from its early years up to its conversion as a university in 1949?"},
                {"role": "assistant", "content": "The University of Southern Philippines Foundation (USPF) has a rich history that dates back to its early years as the Southern Institute. It was founded on May 14, 1927, by a group of individuals who recognized the need for a private, non-sectarian educational institution that would provide high-quality instruction accessible to the average person in the community. The founders of the Southern Institute included: 1. Agustin Jereza, a civil engineer from the State University of Iowa, Virgilio Gonzales: A doctor of medicine from the University of the Philippines, 3. Miguel Sanson: A practicing attorney, 4. Mrs. Natividad Villa-Albino: A school teacher, 5. Felipe Ouano, Fructuoso Ramos, and Hipolito Andrada: Businessmen, 6. Dr. Jose Mirasol is a chemist and former dean of the Cebu Junior College, which was the Cebu branch of the University of the Philippines. Dr. Mirasol served as the first director of the school. Initially named the Southern Institute, the institution was granted a permit to operate a complete elementary course and the first two years of secondary education on May 29, 1927. Classes began with 121 students in a rented building located on Colon Street, Cebu City. Within two years, on August 28, 1929, the school received government recognition for its secondary course and produced its first fifteen graduates. The Southern Institute has experienced growth and development over the years. In 1933, due to an increase in the student population, it moved to its own two-story concrete building on Mabini Street. That same year, the College of Commerce opened with 11 students. Subsequently, in 1935, the College of Liberal Arts, the College of Civil Engineering, and the College of Law were established. On February 19, 1937, the College of Law received government recognition. In 1937, the Southern Institute changed its name to the Southern College. Further expansions took place in the following years. In 1939, the Junior Normal Course, aimed at meeting the demand for elementary school teachers, was introduced. The College of Education was established in 1940, and both the Junior Normal Course and the College of Commerce received government recognition on August 9, 1941. However, the Second World War from 1942 to 1944 had a devastating impact on the school. The campus buildings were destroyed, except for the façade of the Administration Building and the U.S. The Army occupied the campus. After the war, the school was reconstructed using surplus materials obtained from the U.S. Army. In 1945, it reopened at Camputhaw (now Lahug), three kilometers away from the old site. Courses in Liberal Arts, Law, and the College of Education were offered, and in 1946, the College of Commerce and the College of Civil Engineering were reopened. Government recognition for all these courses was renewed and granted in 1947. On July 1, 1949, the Southern College was granted government recognition to operate a postgraduate course in education, specifically the Master of Arts in Education. This recognition paved the way for the institution to achieve university status. Consequently, on July 8, 1949, the name was changed to the University of the Southern Philippines (USP). The graduate courses offered at that time included a Master of Arts in Education, a Master of Arts in English, a Master of Arts in Teaching Sociology, and a Master of Arts in Teaching English. Due to further expansions, the Mabini Campus extended its facilities to V. Gullas (formerly Manalili) and P. Burgos streets. The Sanson and Doa Beatriz Halls housed the Elementary Department, while the Gonzales Hall accommodated the College of Engineering, and there was a separate Home Economics Building. In 1959, the university's stockholders agreed to dissolve the original stock corporation and convert USP into a non-stock, non-profit foundation. On May 28, 1959, the University of the Southern Philippines Foundation was officially registered with the Securities and Exchange Commission (SEC). Recognizing the potential congestion at the Mabini Campus and observing the trend of educational institutions dispersing to the suburbs, Don Agustin Jereza established the USP Lahug Campus in 1962. Located on Salinas Drive, the Lahug Campus has since become the main campus of the University of the Southern Philippines Foundation."},
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

        history = []

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
