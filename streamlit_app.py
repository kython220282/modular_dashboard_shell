import streamlit as st
st.set_page_config(page_title="Modular Dashboard", page_icon = ":bar_chart:",layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title('<Business Name> Performance Dashboard')
def main():
  tab1, tab2, tab3, tab4 = st.tabs(["Upload Data","Overall Performance","Metrics 1","Metrics 2"])
  with tab1:
    st.subheader("Upload Data")
  with tab2:
    st.subheader("Overall Performance")
  with tab3:
    st.subheader("Performance on <Metrics 1>")
  with tab4:
    st.subheader("Performance on <Metrics 2>")


if __name__ == "__main__":
    main()
    
  
