import streamlit as st
st.set_page_config(page_title="Modular Dashboard", page_icon = ":bar_chart:",layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title('Application Name')
st.write('--------')
def main():
  tab1, tab2, tab3 = st.tabs(["Overall Performance","Metrics 1","Metrics 2"])
  with tab1:
    st.header("Overall Performance")

  with tab2:
    st.header("Performance on <Metrics 1>")

  with tab2:
    st.header("Performance on <Metrics 2>")
    
  
