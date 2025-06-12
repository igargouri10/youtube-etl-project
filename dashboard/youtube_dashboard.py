import streamlit as st
import pandas as pd
import sqlite3

# Load data from SQLite
conn = sqlite3.connect("data/youtube_etl.db")
df = pd.read_sql_query("SELECT * FROM youtube_videos", conn)
conn.close()

st.title("📊 YouTube Channel Video Dashboard")
st.write(f"Total Videos: {len(df)}")
st.dataframe(df)

# Publish by day of week
st.subheader("Video Publishing Days")
st.bar_chart(df["published_day_of_week"].value_counts())
