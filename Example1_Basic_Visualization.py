import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/Housing.csv')

# We name our app
st.title("Housing Dataset Exploration")

# We can display the dataset at the top
st.write("### Dataset Overview")
st.write(data)

# Plot a histogram of housing prices vs bedrooms
st.write("### Histogram of Housing Prices")
fig, ax = plt.subplots()
ax.hist(data['price'], bins=30, edgecolor='black')
ax.set_xlabel('Price')
ax.set_ylabel('Frequency')
st.pyplot(fig)