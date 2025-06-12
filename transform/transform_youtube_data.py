import pandas as pd

# Load extracted data
df = pd.read_csv("data/raw/youtube_videos.csv")

# Convert 'published_at' to datetime
df["published_at"] = pd.to_datetime(df["published_at"])

# Add 'published_day_of_week'
df["published_day_of_week"] = df["published_at"].dt.day_name()

# Clean up titles
df["title"] = df["title"].str.strip().str.replace('\n', ' ', regex=True)

# Optional: Sort by publish date
df = df.sort_values(by="published_at", ascending=False)

# Save transformed data
df.to_csv("data/youtube_videos_cleaned.csv", index=False)

print("✅ Transformed data saved to data/youtube_videos_cleaned.csv")
