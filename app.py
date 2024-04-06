import streamlit as st
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

# Load the tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Streamlit UI
input_text = st.text_area("Enter Text", height=100)
generate_button = st.button("Analyze Sentiment")

if generate_button and input_text:
    # Tokenize the input text and prepare it as input to the model
    inputs = tokenizer(input_text, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    sentiment = model.config.id2label[predicted_class_id]

    st.markdown(f"**Sentiment**: {sentiment}")
