from transformers import pipeline
import streamlit as st

model = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", use_pytorch=True, aggregation_strategy="simple")

input_text = st.text_area("Enter Text", height=100)
generate_button = st.button("Identify Entities")

if generate_button and input_text:
    results = model(input_text)
    for result in results:

        entity = f"Entity: {result['entity_group']} (Score: {result['score']:.4f})"
        text = f"Text: {result['word']}"
        st.markdown(f"**{entity}** - {text}")
