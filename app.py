import streamlit as st
from utils import getReview
import time


st.set_page_config(
    page_title="Code Reviewer",
    page_icon="👩🏽‍💻",
    layout="centered",
)


#Title
st.title('Code Reviewer')

#User Input
st.header('User Input')
code=st.text_area('Enter your code')
submit=st.button('Get Review')




#Processing the query
if submit==True:
    review=getReview(code)
    #In progress Animation
    progress_text = "Our expert is in deep thought!. Please Wait😁😁"
    my_bar = st.progress(5, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
   
    if review.text:
        st.write(review.text)
    else:
        st.write('Try again')
    
