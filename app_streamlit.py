import streamlit as st
import pandas as pd

st.set_page_config(
        page_title="Gramedia Book Search Engine",
        layout="wide",
        initial_sidebar_state="expanded",)

def main():
    st.markdown("<h1 style='text-align: center; color: #31333F;'>Gramedia Search Book</h1>",
                unsafe_allow_html=True)
    choice = ""
    search_term = ""
    selbox = ["Author","Title","Book Id"]
    choice = st.selectbox("Search Option", selbox)
    with st.form(key = 'search form'):
        nav1,nav2 = st.columns([5,1])
        with nav1:
            search_term = st.text_input(label = choice)
        with nav2:
            st.text("Search")
            sumbit_search = st.form_submit_button(label='Sumbit')
    if search_term != "":
        #this code will use for get data after search and create them into dataframe
        #df = select(choice, search_term)
        #df = pd.DataFrame(df, columns=['Book ID', 'Title', 'Author', 'Released Year', 'Stock', 'Price'])
        st.success("Your searched for {}".format(search_term))
        #st.table(df) this code for view the data     
    elif search_term == "":
        st.error("No data has input") 

if __name__ == "__main__":
    main()
