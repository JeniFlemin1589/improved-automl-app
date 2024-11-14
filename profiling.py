import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def show_profiling():
    if 'df' in st.session_state:
        st.title("Automated Exploratory Data Analysis")
        
        if st.session_state.df.shape[0] > 10000:
            df_sample = st.session_state.df.sample(n=10000, random_state=42)
            st.warning("Dataset too large, sampling 10,000 rows for profiling.")
        else:
            df_sample = st.session_state.df
        
        profile_report = ProfileReport(df_sample, minimal=True)
        st_profile_report(profile_report)
    else:
        st.error("Please upload a dataset first.")
