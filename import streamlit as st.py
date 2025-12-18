import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Download required NLTK resources (needed on Streamlit Cloud)
nltk.download("punkt")
nltk.download("punkt_tab")

st.set_page_config(page_title="NLTK Tokenizer", layout="centered")

st.title("🧠 NLTK Word Tokenizer")

text = st.text_area(
    "Enter text to tokenize:",
    placeholder="Type or paste text here..."
)

if text:
    try:
        tokens = word_tokenize(text)
        st.subheader("Tokenized Output:")
        st.write(tokens)
    except Exception as e:
        st.error(f"Error during tokenization: {e}")
