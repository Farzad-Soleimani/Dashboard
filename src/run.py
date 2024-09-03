# Moudals
import streamlit as st
import pandas as pd
from io import StringIO
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image

# Sidebar
login_option = st.sidebar.radio('Login/Sign up', ('Login','Sign up'))

if login_option== "Login":
    with st.sidebar.form("login"):
        st.write("Login Here")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("Sign up"):
        st.write("Sign up Here")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        Email = st.text_input('Email:')

        submitted = st.form_submit_button("Sign up")
        if submitted:
            pass

# Banner
banner = Image.open('./data/banner3.webp')
st.image(banner, caption="Sunrise by your soul", width = None)

# Creating Title
st.title(":notebook: Project dashboard")

# Working with data base
with st.expander("Data"):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

        data = json.loads(string_data)
        st.json(data)

#Statistics
#with st.expander("Statistics"):
    #fig, ax = plt.subplots(1, 1, figsize=(10,5))
    #sns.histplot(np.random.randn(100), ax=ax)
    #st.pyplot(fig)

#User_Profile
with st.expander("User Profile"):
    col1, col2 = st.columns(2)
    col1.text_input("name:")
    col2.text_input("Location:")
    st.camera_input('Camera Input', key='camera_input')
