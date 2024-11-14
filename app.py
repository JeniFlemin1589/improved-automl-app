import streamlit as st
import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader
from home import show_home
from user_registration import show_user_registration
from upload import show_upload
from explore import show_explore
from profiling import show_profiling
from ml import show_ml
from download import show_download

# Load the configuration from a YAML file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Sidebar for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Home"

def set_page(page):
    st.session_state.page = page
    st.experimental_rerun()

# Sidebar for navigation
with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("AutoStreamML")
    choice = st.radio("Navigation", ["Home","User Registration","Upload", "Explore","Profiling", "ML", "Download"])
    st.info("This application allows you to build an automated ML pipeline using Streamlit, Pandas Profiling, and PyCaret. And It's Great!")

# Handle page navigation
if choice == "Home":
    st.session_state.page = "Home"
elif choice == "User Registration":
    st.session_state.page = "User Registration"
elif choice == "Upload":
    st.session_state.page = "Upload"
elif choice == "Explore":
    st.session_state.page = "Explore"
elif choice == "Profiling":
    st.session_state.page = "Profiling"
elif choice == "ML":
    st.session_state.page = "ML"
elif choice == "Download":
    st.session_state.page = "Download"

# Home page
if st.session_state.page == "Home":
    show_home()

# User Registration page
if st.session_state.page == "User Registration":
    show_user_registration()

# Check if sourcedata.csv exists
if "df" not in st.session_state and os.path.exists("sourcedata.csv"):
    st.session_state.df = pd.read_csv("sourcedata.csv", index_col=None)

# Upload data
if st.session_state.page == "Upload":
    show_upload()

# Explore pre-loaded datasets
if st.session_state.page == "Explore":
    preloaded_datasets = {
        'Covid': {
            'image_url': 'Covid data/covid.jpg',
            'data_path': 'Covid data/covid.csv'
        },
        'Titanic': {
            'image_url': 'Titanic data/titanic.jpg',
            'data_path': 'Titanic data/titanic.csv'
        },
        'Developer': {
            'image_url': 'Developer data/developer.jpg',
            'data_path': 'Developer data/developer.csv'
        },
        'Weather': {
            'image_url': 'Weather data/weather.jpg',
            'data_path': 'Weather data/weather.csv'
        },
        'Spam': {
            'image_url': 'Spam data/spam.png',
            'data_path': 'Spam data/spam.csv'
        }
    }
    show_explore(preloaded_datasets)

# Profiling
if st.session_state.page == "Profiling":
    show_profiling()

# Machine Learning
if st.session_state.page == "ML":
    show_ml()

# Download model
if st.session_state.page == "Download":
    show_download()
