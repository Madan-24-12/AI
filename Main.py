# import streamlit as st
# import ollama
# import pandas as pd
# import random

# def query_resolution(query):
#     response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": query}])
#     return response['message']['content']

# def generate_content(topic):
#     prompt = f"Generate lecture notes, quizzes, and programming assignments for {topic}."
#     response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": prompt}])
#     return response['message']['content']

# def automated_grading(student_answer, expected_answer):
#     prompt = f"Evaluate the following student response:\n\nStudent Answer: {student_answer}\nExpected Answer: {expected_answer}\nGive feedback and score out of 10."
#     response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": prompt}])
#     return response['message']['content']

# def analyze_performance(student_scores):
#     avg_score = sum(student_scores) / len(student_scores)
#     if avg_score > 8:
#         return "Excellent performance! Keep up the good work."
#     elif avg_score > 5:
#         return "Good performance, but there's room for improvement."
#     else:
#         return "Needs improvement. Consider additional study materials."

# st.title("AI-Powered Virtual Assistant for Technical Teachers")

# menu = st.sidebar.selectbox("Choose Module", ["NLP Query Resolution", "Content Generation", "Automated Grading", "Student Performance Analysis", "Interactive Chatbot"])

# if menu == "NLP Query Resolution":
#     query = st.text_input("Enter your CSE-related question:")
#     if st.button("Get Answer"):
#         answer = query_resolution(query)
#         st.write("### Answer:")
#         st.write(answer)

# elif menu == "Content Generation":
#     topic = st.text_input("Enter the topic:")
#     if st.button("Generate Content"):
#         content = generate_content(topic)
#         st.write("### Generated Content:")
#         st.write(content)

# elif menu == "Automated Grading":
#     student_answer = st.text_area("Enter student answer:")
#     expected_answer = st.text_area("Enter expected answer:")
#     if st.button("Evaluate"):
#         feedback = automated_grading(student_answer, expected_answer)
#         st.write("### Grading Feedback:")
#         st.write(feedback)

# elif menu == "Student Performance Analysis":
#     scores = st.text_area("Enter student scores separated by commas (e.g., 7, 8, 6, 9)")
#     if st.button("Analyze Performance"):
#         student_scores = list(map(int, scores.split(',')))
#         analysis = analyze_performance(student_scores)
#         st.write("### Performance Analysis:")
#         st.write(analysis)

# elif menu == "Interactive Chatbot":
#     chat_input = st.text_input("Ask the chatbot a question:")
#     if st.button("Chat"):
#         chat_response = query_resolution(chat_input)
#         st.write("### Chatbot Response:")
#         st.write(chat_response)
# import streamlit as st
# import ollama
# import speech_recognition as sr # type: ignore
# import pandas as pd
# import random

# def query_resolution(query):
#     response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": query}])
#     return response['message']['content']

# def generate_content(topic):
#     prompt = f"Generate lecture notes, quizzes, and programming assignments for {topic}."
#     response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": prompt}])
#     return response['message']['content']

# def automated_grading(student_answer, expected_answer):
#     prompt = f"Evaluate the following student response:\n\nStudent Answer: {student_answer}\nExpected Answer: {expected_answer}\nGive feedback and score out of 10."
#     response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": prompt}])
#     return response['message']['content']

# def analyze_performance(student_scores):
#     avg_score = sum(student_scores) / len(student_scores)
#     if avg_score > 8:
#         return "Excellent performance! Keep up the good work."
#     elif avg_score > 5:
#         return "Good performance, but there's room for improvement."
#     else:
#         return "Needs improvement. Consider additional study materials."

# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening... Please speak your question.")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
    
#     try:
#         query = recognizer.recognize_google(audio)
#         st.write(f"You said: {query}")
#         return query
#     except sr.UnknownValueError:
#         st.write("Sorry, I could not understand the audio.")
#         return ""
#     except sr.RequestError:
#         st.write("Could not request results, please check your internet connection.")
#         return ""

# st.title("AI-Powered Virtual Assistant for Technical Teachers")

# menu = st.sidebar.selectbox("Choose Module", ["NLP Query Resolution", "Content Generation", "Automated Grading", "Student Performance Analysis", "Interactive Chatbot"])

# if menu == "NLP Query Resolution":
#     if st.button("Speak Now"):
#         query = recognize_speech()
#         if query:
#             answer = query_resolution(query)
#             st.write("### Answer:")
#             st.write(answer)

# elif menu == "Content Generation":
#     topic = st.text_input("Enter the topic:")
#     if st.button("Generate Content"):
#         content = generate_content(topic)
#         st.write("### Generated Content:")
#         st.write(content)

# elif menu == "Automated Grading":
#     student_answer = st.text_area("Enter student answer:")
#     expected_answer = st.text_area("Enter expected answer:")
#     if st.button("Evaluate"):
#         feedback = automated_grading(student_answer, expected_answer)
#         st.write("### Grading Feedback:")
#         st.write(feedback)

# elif menu == "Student Performance Analysis":
#     scores = st.text_area("Enter student scores separated by commas (e.g., 7, 8, 6, 9)")
#     if st.button("Analyze Performance"):
#         student_scores = list(map(int, scores.split(',')))
#         analysis = analyze_performance(student_scores)
#         st.write("### Performance Analysis:")
#         st.write(analysis)

# elif menu == "Interactive Chatbot":
#     if st.button("Speak to Chatbot"):
#         chat_input = recognize_speech()
#         if chat_input:
#             chat_response = query_resolution(chat_input)
#             st.write("### Chatbot Response:")
#             st.write(chat_response)
import streamlit as st
import ollama
import speech_recognition as sr  # type: ignore
import pandas as pd
import random

def query_resolution(query):
    response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": query}])
    return response['message']['content']

def generate_content(topic):
    prompt = f"Generate lecture notes, quizzes, and programming assignments for {topic}."
    response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

def automated_grading(student_answer, expected_answer):
    prompt = f"Evaluate the following student response:\n\nStudent Answer: {student_answer}\nExpected Answer: {expected_answer}\nGive feedback and score out of 10."
    response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

def analyze_performance(student_scores):
    avg_score = sum(student_scores) / len(student_scores)
    if avg_score > 8:
        return "Excellent performance! Keep up the good work."
    elif avg_score > 5:
        return "Good performance, but there's room for improvement."
    else:
        return "Needs improvement. Consider additional study materials."

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Please speak your question.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        query = recognizer.recognize_google(audio)
        st.write(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError:
        st.write("Could not request results, please check your internet connection.")
        return ""

st.title("AI-Powered Virtual Assistant for Technical Teachers")

menu = st.sidebar.selectbox("Choose Module", ["NLP Query Resolution", "Content Generation", "Automated Grading", "Student Performance Analysis", "Interactive Chatbot"])

if menu == "NLP Query Resolution":
    if st.button("Speak Now"):
        query = recognize_speech()
        if query:
            answer = query_resolution(query)
            st.write("### Answer:")
            st.write(answer)

elif menu == "Content Generation":
    topic = st.text_input("Enter the topic:")
    if st.button("Generate Content"):
        content = generate_content(topic)
        st.write("### Generated Content:")
        st.write(content)

elif menu == "Automated Grading":
    student_answer = st.text_area("Enter student answer:")
    expected_answer = st.text_area("Enter expected answer:")
    if st.button("Evaluate"):
        feedback = automated_grading(student_answer, expected_answer)
        st.write("### Grading Feedback:")
        st.write(feedback)

elif menu == "Student Performance Analysis":
    scores = st.text_area("Enter student scores separated by commas (e.g., 7, 8, 6, 9)")
    if st.button("Analyze Performance"):
        student_scores = list(map(int, scores.split(',')))
        analysis = analyze_performance(student_scores)
        st.write("### Performance Analysis:")
        st.write(analysis)

elif menu == "Interactive Chatbot":
    if st.button("Speak to Chatbot"):
        chat_input = recognize_speech()
        if chat_input:
            chat_response = query_resolution(chat_input)
            st.write("### Chatbot Response:")
            st.write(chat_response)
