
from transformers import pipeline
import streamlit as st

model = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", grouped_entities=True)
input_text = st.text_area("Enter Text", height=100)
generate_button = st.button("Identify Entities")
if generate_button:
    if input_text:
        results = model(input_text)
        for result in results:
            st.markdown(f"**Entity**: {result['word']}, **Type**: {result['entity_group']}, **Score**: {result['score']:.4f}")
