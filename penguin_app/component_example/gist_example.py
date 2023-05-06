import streamlit as st 
from streamlit_embedcode import github_gist

st.title("Github Gist Example") 
st.write("Code from Palmer's Penguin Streamlit app.")
github_gist('https://gist.github.com/JasmineLin1205/c13a85b5fc0678666278000d46ba592d')

