import streamlit as st

st.title("Hello People")

name = st.text_input("Enter your name")

if name:
    st.write("Hello,", name)
