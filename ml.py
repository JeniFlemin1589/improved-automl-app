import streamlit as st
from pycaret.classification import setup, compare_models, pull, save_model
from sklearn.preprocessing import LabelEncoder

def show_ml():
    if 'df' in st.session_state:
        st.title("Machine Learning Go Magic!")
        target = st.selectbox('Choose the Target Column', st.session_state.df.columns)
        if st.button('Train Model'): 
            df_cleaned = st.session_state.df.dropna(subset=[target])
            
            class_counts = df_cleaned[target].value_counts()
            valid_classes = class_counts[class_counts >= 2].index
            df_filtered = df_cleaned[df_cleaned[target].isin(valid_classes)]

            if len(df_filtered) < 2:
                st.error("Not enough data to run the model after filtering out classes with less than 2 instances.")
            else:
                df_encoded = df_filtered.copy()
                for col in df_encoded.select_dtypes(include='object').columns:
                    if col != target:
                        le = LabelEncoder()
                        df_encoded[col] = le.fit_transform(df_encoded[col])
                
                setup(df_encoded, target=target)

                set_up = pull()
                st.info("This is the ML Experiment settings")
                st.dataframe(set_up)
                best_model = compare_models()
                compare_df = pull()
                st.info("This is the ML Model")
                st.dataframe(compare_df)
                st.write(best_model)
                save_model(best_model, "best_model")
