import streamlit as st
import pandas as pd

def load_preloaded_data(option, preloaded_datasets):
    dataset_info = preloaded_datasets[option]
    try:
        return pd.read_csv(dataset_info['data_path'], encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(dataset_info['data_path'], encoding='latin1')

def show_explore(preloaded_datasets):
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
    }
    .custom-expander .streamlit-expanderHeader {
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.image("explore.png")
    st.title("Explore Pre-loaded Datasets")
    for dataset_name, dataset_info in preloaded_datasets.items():
        with st.expander(f"{dataset_name} Dataset", expanded=False):
            st.image(dataset_info['image_url'], caption=dataset_name, use_column_width=True)
            st.write(f"### {dataset_name}")
            df_sample = load_preloaded_data(dataset_name, preloaded_datasets).head()
            st.dataframe(df_sample)
            if st.button(f"Load {dataset_name} Dataset"):
                st.session_state.df = load_preloaded_data(dataset_name, preloaded_datasets)
                st.session_state.df.to_csv("sourcedata.csv", index=None)
                st.success(f"{dataset_name} dataset loaded successfully!")
                st.session_state.page = "Upload"
                st.experimental_rerun()