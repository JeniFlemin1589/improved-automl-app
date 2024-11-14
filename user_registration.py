import streamlit as st

def show_user_registration():
    st.title("User Registration")
    st.write("Sign in or Log in using your email account or Google account.")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register / Log In"):
        if email == "jeni@gmail.com" and password == "1234":
            st.session_state.auth = True
            st.success("Logged in successfully!")
            st.session_state.page = "Explore"
            st.experimental_rerun()
        else:
            st.error("Invalid email or password")
