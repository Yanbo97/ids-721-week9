from transformers import pipeline
import streamlit as st

model_name = "sshleifer/distilbart-cnn-12-6"
model = pipeline("summarization", model=model_name)

input_text = st.text_area("Enter Text", height=100)
generate_button = st.button("Summarize Text")
if generate_button and input_text:
    output_text = model(input_text, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
    st.markdown(f"**Summary**: {output_text}")
