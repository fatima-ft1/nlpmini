import streamlit as st
from summa import summarizer

def main():
    st.title("Text Summarizer")

    text = st.text_area("Input Text For Summary", height=300)
    summary_ratio = st.slider("Summarize Ratio", 0.1, 1.0, 0.5, 0.05)
    
    if st.button("Summarize"):
        summary_result = summarizer.summarize(text, ratio=summary_ratio)
        st.success(summary_result)

if __name__ == '__main__':
    main()

