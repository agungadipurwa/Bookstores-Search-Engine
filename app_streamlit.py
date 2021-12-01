import streamlit as st
from book_search import *
import pandas as pd

st.set_page_config(
        page_title="Gramedia Book Search Engine",
        layout="wide",
        initial_sidebar_state="expanded",)

def main():
    st.markdown("<h1 style='text-align: center; color: #31333F;'>Gramedia Search Book</h1>",
                unsafe_allow_html=True)
    with st.form(key = 'Search From',clear_on_submit=True):
        nav1,nav2,nav3 = st.columns([1,5,1])
        with nav1:
            choice_term = st.selectbox(label= 'Option',options=['Author','Title','Book Id'])
        with nav2:
            search_term = st.text_input(label = 'By')
        with nav3:
            st.text("Search")
            sumbit_search = st.form_submit_button(label='Sumbit')
    if sumbit_search:
        #this code will use for get data after search and create them into dataframe
        df = select(choice_term, search_term)
        st.success("Your searched for {}".format(search_term))
        st.dataframe(df)
    elif search_term == "":
        st.error("No data has input") 
    
if __name__ == "__main__":
    main()
