import streamlit as st

def show_download():
    with open("best_model.pkl", 'rb') as f:
        st.download_button("Download the file", f, "Trained_model.pkl")
