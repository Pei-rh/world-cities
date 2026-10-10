import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

# 1. title (replace [Your Name] with your own name)
st.title('California Housing Data (1990) by Ruohan Pei')

df = pd.read_csv('housing.csv')

# 2. slider to filter by median house value
min_value = st.slider('Minimal Median House Value', 0, 500001, 200000)  # min, max, default

# 3. subheader pointing to the sidebar filters
st.subheader('See more filters in the sidebar:')

# 4. sidebar multiselect to filter by location type
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),  # options
    df.ocean_proximity.unique())  # defaults

# 5. sidebar radio to filter by income level
income_filter = st.sidebar.radio(
    'Choose income level',
    ('Low', 'Medium', 'High'))

# filter by median house value
df = df[df.median_house_value >= min_value]

# filter by location type
df = df[df.ocean_proximity.isin(location_filter)]

# filter by income level
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income >= 4.5]

# 6. show the filtered districts on a map
st.map(df)

# 7. histogram of median house value for the filtered districts
st.subheader('Histogram of Median House Value')
fig, ax = plt.subplots(figsize=(10, 5))
df.median_house_value.plot.hist(ax=ax, bins=30)
ax.set_xlabel('Median House Value')
st.pyplot(fig)
