# Name: Brendan Brady, Lina Botero
# Library: Streamlit
# URL: https://github.com/lbotero1/OIM_7502_Streamlit_Midterm
# Description: Streamlit is a Python library designed to simplify the process of building web apps.
# With its intuitive syntax and seamless integration with popular data science libraries,
# Streamlit empowers developers and data scientists to create interactive and visually appealing applications.
# Whether you're visualizing data, prototyping machine learning models, or building dashboards,
# Streamlit provides a streamlined development experience, allowing you to focus on your ideas rather than the
# complexities of web development.

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/Housing.csv')

st.write("First 5 Rows of the Dataset")
st.write(data.head())
# Show summary statistics
st.write("Summary Statistics")
st.write(data.describe())

# Select box for choosing a column
column = st.selectbox('Select column', data.columns)

# Display selected column data
st.write(data[column])

# Select columns for visualization
col1 = st.selectbox('Select first column for plot', data.columns)
col2 = st.selectbox('Select second column for plot', data.columns)

# Plotting with seaborn
sns.jointplot(x=col1, y=col2, data=data, kind='scatter')
st.pyplot(plt)

# Function to plot a correlation matrix
def plot_correlation(data):
    corr = data.corr()
    plt.figure(figsize=(10,10))
    sns.heatmap(corr, annot=True, fmt=".2f")
    st.pyplot(plt)

# Button to show correlation matrix
if st.button('Show Correlation Matrix'):
    plot_correlation(data)

# Select a column for filtering
filter_column = st.selectbox('Select Column to Filter', data.columns)

# Slider for selecting range
min_value, max_value = st.slider('Filter range', float(data[filter_column].min()), float(data[filter_column].max()),
                                 (float(data[filter_column].min()), float(data[filter_column].max())))

# Filtering the data
filtered_data = data[(data[filter_column] >= min_value) & (data[filter_column] <= max_value)]
st.write(filtered_data)