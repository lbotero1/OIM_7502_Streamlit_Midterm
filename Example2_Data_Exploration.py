import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('data/Housing.csv')

# Now we are adding some colors.
# Set plot style to magenta
sns.set_palette(["magenta", "cyan", "lime", "orange"])

# Define custom groups for areas based on square footage
area_groups = {
    'Small': (1650, 5000),
    'Medium': (5001, 10000),
    'Large': (10001, 16200)
}

# Set page config
st.set_page_config(
    page_title="Housing Dataset Exploration",
    page_icon=":house:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title of the app
st.title("Housing Dataset Exploration")

# Sidebar for user input
st.sidebar.title("Filter Data")

# Filter by area group
area_group = st.sidebar.selectbox("Area Group", options=list(area_groups.keys()), key="area_group")

# Get square footage range for the selected group
group_range = area_groups[area_group]
min_range, max_range = group_range

# Filter by square footage range
filtered_data_area = data[(data['area'] >= min_range) & (data['area'] <= max_range)]

# Display filtered data by area group
if not filtered_data_area.empty:
    st.markdown(f'<div style="color: #DC143C;">### Filtered Data for {area_group} Areas</div>', unsafe_allow_html=True)
    st.dataframe(filtered_data_area)
else:
    st.markdown(f'<div style="color: #DC143C;">### No data matches the selected area group filters.</div>',
                unsafe_allow_html=True)


# Scatter Plot: Explore relationship between price and square footage
st.write(f'<div style="color: #DC143C;">### Scatter Plot of Price vs Area')
scatter_plot = plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='price', y='area', alpha=0.7)
plt.xlabel('Price')
plt.ylabel('Area')
st.pyplot(scatter_plot)

# Violin Plot: Visualize distribution of price across different areas
st.write(f'<div style="color: #DC143C;">### Violin Plot of Price Distribution across Different Areas')
violin_plot = plt.figure(figsize=(10, 6))
sns.violinplot(data=data, x='area', y='price')
plt.xticks(rotation=45)
plt.xlabel('Area')
plt.ylabel('Price')
st.pyplot(violin_plot)

# Area Plot: Visualize trends over time or across different categories
# In this case, let's visualize the trend of price across different areas
st.write(f'<div style="color: #DC143C;"### Area Plot of Price Trends across Different Areas')
area_plot_data = data.groupby('area')['price'].mean().reset_index()
area_plot = plt.figure(figsize=(10, 6))
sns.lineplot(data=area_plot_data, x='area', y='price', marker='o')
plt.xticks(rotation=45)
plt.xlabel('Area')
plt.ylabel('Average Price')
st.pyplot(area_plot)

# Filter by number of bedrooms and bathrooms for average price
st.sidebar.title("Filter by Bedrooms and Bathrooms")

# Filter by number of bedrooms
bedrooms = st.sidebar.slider("Number of Bedrooms", min_value=1, max_value=10, value=5, key="bedrooms")

# Filter by number of bathrooms
bathrooms = st.sidebar.slider("Number of Bathrooms", min_value=1, max_value=10, value=2, key="bathrooms")

# Apply filters
filtered_data_bed_bath = filtered_data_area[
    (filtered_data_area['bedrooms'] == bedrooms) & (filtered_data_area['bathrooms'] == bathrooms)]

# Display filtered data
if not filtered_data_bed_bath.empty:
    st.markdown('<div style="color: #DC143C;">### Filtered Data</div>', unsafe_allow_html=True)
    st.dataframe(filtered_data_bed_bath)

    # Calculate average price
    average_price = filtered_data_bed_bath['price'].mean()
    st.markdown(f'<div style="color: #DC143C;">Average Price: ${average_price:.2f}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div style="color: #DC143C;">### No data matches the selected filters.</div>', unsafe_allow_html=True)


# Create separate plots for each variable
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot for Bedrooms
sns.histplot(data['bedrooms'], ax=axs[0, 0], kde=True)
axs[0, 0].set_title('Bedrooms')

# Plot for Bathrooms
sns.histplot(data['bathrooms'], ax=axs[0, 1], kde=True)
axs[0, 1].set_title('Bathrooms')

# Plot for Area
sns.histplot(data['area'], ax=axs[1, 0], kde=True)
axs[1, 0].set_title('Area')

# Plot for Price
sns.histplot(data['price'], ax=axs[1, 1], kde=True)
axs[1, 1].set_title('Price')

# Adjust layout
plt.tight_layout()

# Display the plots
st.pyplot(fig)
