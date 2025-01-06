import streamlit as st
st.set_page_config(page_title="Modular Dashboard", page_icon = ":bar_chart:",layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title('<Business Name> Performance Dashboard')
def main():
  tab1, tab2, tab3, tab4 = st.tabs(["Upload Data","Overall Performance","Metrics 1","Metrics 2"])
  with tab1:
    col1, col2 = st.columns([1,3])
    with col1:
      with st.container():
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
          dataframe = pd.read_csv(uploaded_file)
          st.write(dataframe)
    with col1:
      with st.container():
        st.subheader("Review Data uploaded")
  with tab2:
    st.subheader("Overall Performance")
  with tab3:
    st.subheader("Performance on <Metrics 1>")
  with tab4:
    st.subheader("Performance on <Metrics 2>")


if __name__ == "__main__":
    main()
    
  
