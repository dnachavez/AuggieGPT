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
                {"role": "user", "content": "List the administration of USPF"},
                {"role": "assistant", "content": "Here is a list of the university administration at the University of Southern Philippines Foundation (USPF). Board of Trustees: Atty. Paulino A. Yabao, JD (Chairman), Fr. Dionisio M. Miranda, SVD (Vice Chairman), Mr. Archibald V. Villa (Treasurer), Mrs. Teresita V. Ponce (Member), Mr. Jeffrey L. Villa (Member), Ms. Katherine V. Ponce (Member), Mr. Rolando L. Villa (Member), Mr. Michael Luis L. Villa (Member), Atty. Tomas V. Alonso (Member), Mr. Francis Christopher Duane E. Villa (Member), Atty. Peter B. Cañamo, LLM (Corporate Secretary). University Officials: Atty. Paulino A. Yabao, JD (University President), Engr. Antonio B. Lapingcao, Jr. (Vice President, Administration), Dr. Ernesto L. Alolor (Vice President, Academic Affairs), Mrs. Rosalina J. Sepulveda (Director, Finance), Mr. Philip Roy G. Yap, CPA (Director, Comptrollership), Ms. Alma Corazon A. Alfafara (Manager, Human Resources Management & Development). University Council: Mr. Charles Roy P. Baguio (Assistant Vice President Academic Affairs, Director, Student Affairs Services), Mrs. Maria Liza Gabriel (University Registrar), Mr. Joeriz B. Arnejo (Internal Auditor, Data Privacy Officer), Mrs. Alma Corazon A. Alfafara (Manager, Human Resources Management & Development), Mr. Boi Archievald A. Ranay (Manager, Information & Communications Technology), Mrs. Elita L. Cui, RGC (Director, Guidance & Testing Services), Mr. Glen P. Albutra (Director, Sports & Cultural Programs), Mrs. Jesusa A. Perez (Manager, Learning Resource Center), Mr. Edgar E. Gahisan, RN, MN, LPT (Director, Community Extension Services), Mrs. Judith M. Eparwa (Director, Communications, Publications & Marketing), Dr. Philip D.R. Macugay, DSS (Director, Research, Planning & Development), Engr. Fondador D. Mendoza Jr. (Director, Quality Assurance), Mr. Nelson M. Dinglasa (Management Accountant), Engr. Victor O. Maldo (Manager, Facilities & Infrastructure Services), Mr. Abundio Ray M. Navares (Manager, Health, Safety & Security Services), Mr. Brian James D. Jereza (Manager, Procurement), Mrs. Grace C. Clabesillas (Manager, Business Resource Center), Mr. Nestor C. Saballa (Manager, USPF Dormitory), Mr. Richy Lloyd M. Tan (Assistant to the Vice President Academic Affairs), Ms. Faye Coleen R. Suyao (Chairperson, Research Ethics Committee). Academic Heads: Dr. Ernesto L. Alolor (Dean, Graduate School), Dr. Janet A. Arcana (Dean, College of Teacher Education, Arts & Sciences), Dr. Venus M. Empuerto (Dean, School of Business & Accountancy), Atty. Peter B. Cañamo, LLM (Dean, School of Law), Mrs. Merlyn A. Ouano, RN (Dean, College of Health Sciences), Engr. Alfredo B. Arenajo (Dean, College of Engineering & Architecture), Mr. Gian Carlo S. Cataraja (OIC, College of Computer Studies), Mrs. Rosario E. Sequitin, MSSW (Dean, College of Social Work), Mrs. Arlene B. Roldan, MAEd (Principal, Senior High School - Lahug Campus), Mrs. Maura A. Villamor, MAEd (Principal, Junior High School - Lahug Campus & Basic Education - Mabini Campus), Dr. Elaine May S. Patiño (Principal, Elementary - Lahug Campus), Mr. Robiel R. Coyoca (Assistant Principal - Mabini Campus), Dr. Lucio A. Pulmones (Assistant Dean, Graduate School)."},
                {"role": "user", "content": "What is the vision?"},
                {"role": "assistant", "content": "The vision of the University of Southern Philippines Foundation (USPF) is to be a transformative learning institution of global lifelong learners."},
                {"role": "user", "content": "What is the mission?"},
                {"role": "assistant", "content": "The mission of the University of Southern Philippines Foundation (USPF) is to provide a value-laden quality education that fosters the development of ethical, innovative, competent, and socially responsive individuals."},
                {"role": "user", "content": "What is the goal?"},
                {"role": "assistant", "content": "The goal of the University of Southern Philippines Foundation (USPF) is to transform into a dynamic learning institution that aligns with global standards in education and the work environment."},
                {"role": "user", "content": "What are the core values?"},
                {"role": "assistant", "content": "The University of Southern Philippines Foundation (USPF) upholds the following core values: 1. Professionalism: At USPF, professionalism is paramount. We uphold a high standard of conduct and competence in all our interactions and endeavors, ensuring professionalism in our dealings at all times and in all contexts., 2. Integrity: We value integrity as a fundamental principle. Integrity is the foundation of our actions, and we strive to keep our integrity intact and untarnished. We act with honesty, transparency, and ethical behavior in all aspects of our work., 3. Excellence: USPF is committed to the pursuit of excellence. We strive for excellence in the performance of our tasks, be it in teaching, research, administration, or any other field. We consistently seek improvement, innovation, and the highest quality in everything we do., 4. Social Responsibility: Recognizing our role as an educational institution, we embrace social responsibility. We actively engage with our community and society at large, taking part in initiatives that contribute positively to the well-being and development of our local and global communities. We aim to make a difference and promote positive change through our actions and initiatives."},
                {"role": "user", "content": "What is Augi?"},
                {"role": "assistant", "content": "Augi is a ChatGPT-powered chatbot assistant"},
                {"role": "user", "content": "Who created Augi?"},
                {"role": "assistant", "content": "Dan Chavez, a BS Computer Science student at USPF College of Computer Studies (CCS) created Augi, a GPT-powered chatbot assistant."},
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
        st.set_page_config(page_title="AugiGPT", page_icon="agustinjereza.png", layout="wide")

        # Display an image
        img = Image.open("agustinjereza.png")
        new_size = (150, 150)
        img = img.resize(new_size)
        st.image(img)

        # Display the chatbot information
        st.markdown("# Hello, I'm Augi! How can I assist you today?")
        st.markdown("## Augi is a ChatGPT-powered chatbot assistant")
        st.markdown("This chatbot assistant is capable of providing answers to questions specifically about the **University of Southern Philippines Foundation (USPF)**.")

        # Collect user input
        user_input = st.text_area("Input your question:", height=5)

        # Process the input and display the response when the 'Submit' button is pressed
        history = []
        if st.button("Submit"):
            history = append_history(history, ("You: " + user_input))
            output = get_reply(user_input)
            if output is not None:
                history = append_history(history, ("Augi: " + output))
                for item in history:
                    st.write(item)

        # Display additional information
        st.markdown("-----------\n\nThis project of [Dan Chavez](https://www.dnachavez.ph) leverages the capabilities of generative AI with specific knowledge on a set of topics. Similar to ChatGPT, it can engage the user in a human-like conversation. Through the use of prompt engineering, the AI has been trained with specific information beyond the general knowledge base of ChatGPT.")
        st.markdown("\n\n\nCopyright © 2023 University of Southern Philippines Foundation")
        st.markdown("\n\n\n**Disclaimer:** Augi may produce inaccurate information about people, places, or facts, especially if the question is outside the scope of topics it was trained on.")
        st.markdown("*Created with ❤️ from Cebu City, Philippines*")

    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    app()
