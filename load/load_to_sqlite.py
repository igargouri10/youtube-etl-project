import pandas as pd
import sqlite3

# Load the transformed CSV
df = pd.read_csv("data/youtube_videos_cleaned.csv")

# Connect to (or create) the SQLite database
conn = sqlite3.connect("data/youtube_etl.db")

# Load data into a table
df.to_sql("youtube_videos", conn, if_exists="replace", index=False)

# Close the connection
conn.close()

print("✅ Data loaded into SQLite database: data/youtube_etl.db")
