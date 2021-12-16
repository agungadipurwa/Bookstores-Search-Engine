import streamlit as st
from book_search import *
import pandas as pd

st.set_page_config(
        page_title="Gramedia Book Search Engine",
        layout="wide",
        page_icon="books",
        initial_sidebar_state="expanded",)

def main():
    #31333F for Light Theme
    #FFFFFF for Dark Theme
    st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>Gramedia Search Book</h1>",
                unsafe_allow_html=True)
    with st.form(key = 'Search From',clear_on_submit=False):
        nav1,nav2,nav3 = st.columns([1,5,1])
        with nav1:
            choice_term = st.selectbox(label= 'Options',options=['Title','Author','Book Id'])
        with nav2:
            search_term = st.text_input(label = 'Search by')
        with nav3:
            st.text("Search")
            submit_search = st.form_submit_button(label='Go')

    if submit_search == True and search_term == "":
        st.error("No data has input")

    elif submit_search:
        #Check the input match or not, if you input an book id as string you will get value error
        try:
            df = select(choice_term, search_term)
        #handling value error after input book id as string
        except ValueError:
            if choice_term == "Book Id":
                try:
                    print(int(search_term))
                except:
                    st.error("You only can search a Book Id using a number")
        else:
            df = select(choice_term, search_term)
            st.success("Your searched for {} in {}".format(search_term, choice_term))
            st.table(df)
    
if __name__ == "__main__":
    main()
