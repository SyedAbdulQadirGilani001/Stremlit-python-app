import streamlit as st
import numpy as np

# Set page title
st.set_page_config(page_title="Eli Random Number Generator")

# Set page header
st.title("Eli Generate Random Number Game")

# Set sidebar options
option = st.sidebar.selectbox("Select an option", ("Uniform Distribution", "Normal Distribution"))

# Generate random numbers based on selected option
if option == "Uniform Distribution":
    start = st.sidebar.number_input("Start", value=0)
    stop = st.sidebar.number_input("Stop", value=1)
    num_samples = st.sidebar.number_input("Number of samples", value=10)
    random_nums = np.random.uniform(start, stop, num_samples)
elif option == "Normal Distribution":
    mean = st.sidebar.number_input("Mean", value=0)
    std = st.sidebar.number_input("Standard deviation", value=1)
    num_samples = st.sidebar.number_input("Number of samples", value=10)
    random_nums = np.random.normal(mean, std, num_samples)

# Display random numbers
st.write("Random Numbers:")
st.write(random_nums)
