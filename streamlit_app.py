import streamlit as st
import pandas as pd

st.set_page_config(page_title="Modular Dashboard", page_icon = ":bar_chart:",layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title('<Business Name> Performance Dashboard')
def main():
  tab1, tab2, tab3, tab4 = st.tabs(["Upload Data","Overall Performance","Metrics 1","Metrics 2"])
  with tab1:
    with col1:
      with st.container():
        uploaded_file = st.file_uploader("Choose a file (CSV or Excel)", type=["csv", "xlsx"])
        df = None
        if uploaded_file is not None:
          if uploaded_file.name.endswith('.csv'):
            try:
              df = pd.read_csv(uploaded_file)
            except Exception as e:
              st.error(f"Error reading CSV file: {e}")
          elif uploaded_file.name.endswith('.xlsx'):
            try:
              df = pd.read_excel(uploaded_file)
            except Exception as e:
              st.error(f"Error reading Excel file: {e}")
    with col2:
      with st.container():
        st.write("Review Data Uploaded:")
        if df is not None:
            edited_df = st.data_editor(df)
            st.write("Edited DataFrame:")
            st.write(edited_df)
        else:
            st.info("No file uploaded or file could not be processed.")
  with tab2:
    st.subheader("Overall Performance")
  with tab3:
    st.subheader("Performance on <Metrics 1>")
  with tab4:
    st.subheader("Performance on <Metrics 2>")


if __name__ == "__main__":
    main()
    
  
