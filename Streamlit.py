import streamlit as st
from rag.answer import get_answer

st.title("GenAI Document Assistant...!")

question = st.text_input("Ask a question about your documents.^^^...!")

if st.button("Submit") and question:
    with st.spinner("Generating answer..."):
        answer = get_answer(question)

    st.write(answer)