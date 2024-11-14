import streamlit as st
import pandas as pd

def show_upload():
    st.title("Upload your data for modeling!")
    file = st.file_uploader("Upload your file here")
    if file:
        st.session_state.df = pd.read_csv(file, index_col=None)
        st.session_state.df.to_csv("sourcedata.csv", index=None)
    if "df" in st.session_state:
        st.dataframe(st.session_state.df)
