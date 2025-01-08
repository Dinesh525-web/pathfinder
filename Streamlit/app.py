import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Dinesh,")

st.write(" welcome to this streamlit powered Zone where you can make interective web pages in easy way")

age = st.slider("what is your age?", 0,21,85)
st.write("you're ", age, "years old")

data = pd.DataFrame(
    np.random.randn(50,6), columns=["a","b","c","d","e","f"]
)

chart = st.line_chart(data)

data_df = pd.DataFrame({
    "1" : [1,2,3,4,5],
    "2" : [5,6,7,8,9]
})

st.write(data_df)

uploaded_file = st.file_uploader("choose the CSV file", type = "csv")

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)
    st.write(df1)