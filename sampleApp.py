import streamlit as st
import pandas as pd
import numpy as np

# -- App Title and Description ---
st.title("My First Streamlit App")
st.write("This is Sample app by KB to demonstarte the basic functionlitites of Streamlit")

# -- Interactive Widgets in the Sidebar --- 
st.sidebar.header("User Input Features")

# -- Text Input --- 
user_name = st.sidebar.text_input("What is ur name ?", "Mr Kulbhushan")

# -- Slider -- 
age = st.sidebar.slider("Select your age ",0,100,30)

# -- SelectBox ---
favorite_color=st.sidebar.selectbox("what is your favorite color ? ",["Blue",'Red','Green',"Black"])

# -- Main Page content -- 
st.header(f"Welcome ,{user_name}!")
st.write(f"You are {age} years old and your favorite color is {favorite_color}.")

# -- Displaying Data -- 
st.subheader("Here is some randon stats: ")

# Create Sample DataFrame
data = pd.DataFrame(np.random.rand(10,5),columns=('column %d' % i for i in range(5)))
st.dataframe(data.head())

# -- checkbox to show and hide content 

if st.checkbox("show raw data"):
    st.subheader("Raw Data")
    st.write(data.head())

# -- Button to trigger an action
if st.button("HOLLA !!"):
    st.write(" hey, Hi !!, Hello there !")
else:
    st.write("Thanks Bye !!")