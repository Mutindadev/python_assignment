# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the dataset
df = pd.read_csv('metadata.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df = df.dropna(subset=['publish_time'])
df['year'] = df['publish_time'].dt.year

# Streamlit title
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research publications interactively.")

# Year filter
year_range = st.slider("Select publication year range", 2019, 2022, (2020, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Display filtered dataset
st.subheader("Sample of Filtered Papers")
st.dataframe(filtered_df[['title', 'journal', 'year']].head(10))

# Publications by year chart
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color='skyblue')
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Word cloud
text = " ".join(filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig_wc, ax_wc = plt.subplots(figsize=(10,5))
ax_wc.imshow(wordcloud, interpolation='bilinear')
ax_wc.axis('off')
st.subheader("Word Cloud of Paper Titles")
st.pyplot(fig_wc)
