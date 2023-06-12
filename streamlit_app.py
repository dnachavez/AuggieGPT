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
                {"role": "user", "content": "What are history milestones of WVSU since 1949?"},
                {"role": "assistant", "content": "Since its conversion to a university in 1949, the University of Southern Philippines Foundation (USPF) has achieved several milestones and witnessed significant developments. In 1970, Engr. Oscar Jereza Sr. formally assumed the position as the President of the University of Southern Philippines. During the same year, the Master of Laws was offered and in 1975, Master of Science in Social Work was added in the graduate school curricular offerings. In 1977, the University celebrated its Golden Jubilee. In 1986, the Graduate School expanded with the opening of the Doctor of Education program. On January 25, 1989, fire gutted the Administration Building at the Mabini Campus that housed the library and the administrative offices. In 1989-90, the University President, Engr. Oscar Jereza Sr., announced the decision reached by the Board of Trustees to temporarily stop operations in all levels at the Mabini Campus. This was aimed at cutting down on cost by concentrating in one campus; that is, the Lahug Campus. Recognizing the moral obligation of the institution towards the students, classes were conducted for all graduating students at the Lahug Campus during 1990-91. No new enrollees, however, were admitted to college. By 1991-92, the university, under the leadership of the new president, Dr. Ronald R. Duterte, decided to reopen college operations phasing in the courses by year levels; that is, first year of all recognized courses was offered during this school year; first and second year by 1992-93, and so on until all years are opened. In February 1995, USPF opened the non-academic skills-based Continuing Education Department, now known as the Learning Resource Center, in partnership with the Manpower Resource Center. In August 1996, the USP Alumni Hall, which houses the famous Rizaliana Museum, was inaugurated. In 1995-96, Bachelor of Science in Accountancy was given Government Recognition to conduct and operate the said course. In June 1999, the College of Law re-opened and a new graduate program, Master of Science in Environmental Management, was offered. On January 28, 2003, the Commission on Higher Education (CHED) issued a permit for USPF to open and conduct the First Year of the four-year Bachelor of Science in Nursing starting June 2003. On March 5, 2003, CHED issued Government Recognition No. 104 s. 2003 to conduct and operate the four-year Bachelor of Science in Information Technology (BSIT) course, effective SY 2003-2004. Two years after the groundbreaking for the Agustin Jereza Building, on January 6, 2004, it already became home to the College of Nursing, College of Law, College of Computer Studies and Information Technology, the College of Engineering and Architecture, and the Escolastico Duterte Library. Additional courses opened during the School Year 2004–2005, specifically Bachelor of Science in Office Administration, Bachelor of Science in Pharmacy, Diploma in Special Education, and Diploma in Professional Education. On June 10, 2005, CHED issued Government Recognition to conduct and open the Post Baccalaureate Diploma in Community Development and Bachelor of Science Entrepreneurship. On December 1, 2005, the Board of Trustees appointed Dr. Alicia P. Cabatingan as the new University President following the death of Dr. Ronald R. Duterte in November 2005. Dr. Cabatingan paved the way for the PACUCOA Accreditation of the different programs of the university. In February 2006, the College of Arts and Sciences and the College of Education successfully passed the PACUCOA Level I Accreditation. During the school year 2007-2008, USPF topped in two of the most prestigious licensure exams in the country. In the same year, the university processed the accreditation of the School of Business and Management, the College of Computer Studies and Information Technology, and the Basic Education departments of the Mabini and Lahug campuses. On July 1, 2017, after the retirement of Dr. Alicia P. Cabatingan, Atty. Paulino A. Yabao was installed as the new University President, who continued the efforts in further improving the University’s academic reputation. In 2017, the installation of CCTVs in the Lahug Campus was completed by the Health, Safety, & Security department in 2017. The SHS Lahug achieved a 100% TESDA NCII ASSESSMENT passing rate for all their Technical Vocational Livelihood courses. The College of Nursing got a 100% Passing Percentage in the June 2017 Philippine Nurse Licensure Examination (PNLE), and 87.50% in the November 2017 PNLE. The SHS Lahug held their first commencement exercises in March 2018. In June 2018, the Elementary Lahug campus received a reissuance of DepEd Government Recognition. The university also began test use of Canvas LMS in SHS for the school year. The improved board/bar ops program to improve the passing performance of courses with government licensure examinations was launched on August 28, 2018. The College of Nursing Class of 2018 earned a 81.25% passing rate in the Philippine Nurse Licensure Examination (PNLE). Starting the second semester of School Year 2018-2019, the University was granted by CHED an authority to offer ETEEAP in Business Management courses. In December 2018, the College of Computer Studies won the first prize for the Lockton Legacy on innovative research, which was awarded in January in 2019 and recognized by PACUCOA in December 2020. In May 2019, the Quality Assurance Office underwent reorganization. The Center for Research, Planning & Development and its research program also underwent a reorganization during the first semester of SY 2019-2020, subsequently necessitating the creation of the Research Ethics Committee during the same semester. Starting June 2019, the SHS and Tertiary department began using Canvas LMS. In August 2019, the College of Social Work placed Top 5 and 7 in the Social Worker Licensure Examination. The School of Business and Management Master in Business Administration program was granted Government Recognition (GR) in the same month. On September 10–12, 2019, the following programs were visited and granted the following PACUCOA accreditations: Bachelor of Science in Nursing     -     Level I Accredited, Bachelor of Science in Social Work   -  Level  I Accredited, Bachelor of Elementary education   -   Level II 2nd Reaccredited, Elementary Lahug    -    Level III First Reaccredited, High School  Lahug  -   Level III First Reaccredited. Also, the Learning Resource Center was re-assessed by TESDA and was authorized to continue as a TESDA Accredited Assessment Center for the following programs: Food & Beverage Service NC II, Bread & Pastry Production NC II, Barista NC II, Cookery NC II, and Housekeeping NC II.In November 2019, the Elementary Lahug campus received PACUCOA Level III Reaccredited Status. The College of Nursing Class of 2019 earned a 90.91% passing rate in the Philippine Nurse Licensure Examination (PNLE). On November 13, 2019, USPF was granted donee status by the Philippine Council for NGO Certification, Inc. In 2019, the Health, Safety, & Security department initiated the University Disaster Risk Reduction Management Team (UDRRMT) and completed installation of CCTVs in both campuses. In January 2020, the College of Nursing was granted PACUCOA Level 1 accreditation. On February 21, 2020, the Bureau of Internal Revenue granted USPF certified donee status. The Guidance and Testing Services Center inked a partnership with Tanglaw Mental Health to optimize COVID-19 mental health support in 2020. In August 2020, the Basic Education department started using C&E's Excello and Kite LMS. SBM’s Bachelor of Science in Management Accounting (BSMA) was granted Temporary Permit (TP) for First Year to Third Year starting School Year 2020-2021. In December 2020, the PACUCOA recognized the Elementary School Lahug as the first Elementary program to have been granted LIII Reaccredited Status in Region VII and JHS Lahug as the first High School program to have been granted LIII Reaccredited Status in Region VII. SHS Lahug continues to achieve 100% TESDA NCII ASSESSMENT passing rate for all their Technical Vocational Livelihood courses. The School of Business and Accountancy Bachelor of Science in Entrepreneurship was granted a Government Permit effective First Semester of SY 2021-2022. The Mabini campus underwent significant renovations in preparation for the PACUCOA Level II 2nd Reaccreditation, which was successfully conducted in the second semester of School Year 2020-2021. The Sports and Cultural Programs consistently garner awards at the National PRISAA, Regional PRISAA, CESAFI, Cebu City Olympics, and CVIRAA. This 2021, the University of Southern Philippines Foundation celebrates 94 years as an academic institution and 72 years as a university staying true to its commitment to serve the nation by producing professionals in different fields of specialization. USPF continues to be a premiere educational institution that responds to the high demands of producing globally competitive graduates, upholding the values of professionalism, integrity, excellence, and social responsibility. Throughout its history, USPF has continually evolved, expanded its program offerings, and strived for academic excellence while adapting to the changing needs and demands of the educational landscape."},
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
        history = []
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
