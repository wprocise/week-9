# app.py
import streamlit as st
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load("sentiment_model.pkl")

model = load_model()

# Streamlit UI
st.title("🏈 Simple Sentiment Analysis App")
st.write("Enter a sentence below to analyze its sentiment:")

# Input box
user_input = st.text_area("Your text:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([user_input])[0]
        if prediction == "positive":
            st.success("Sentiment: Positive")
        else:
            st.error("Sentiment: Negative")


