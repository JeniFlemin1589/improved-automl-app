import streamlit as st

def show_home():
    st.title("Welcome to Auto ML App")
    st.image("home.jpg")
    if st.button("Log IN/Sign IN"):
        st.session_state.page = "User Registration"
        st.experimental_rerun()

    st.write("""
        This application allows you to build an automated ML pipeline using Streamlit, Pandas Profiling, and PyCaret.
        Navigate through the options on the left to get started!
    """)
    st.info("AUTO ML DEEP DIVE IN! EXPLORE AND ENJOY!")
