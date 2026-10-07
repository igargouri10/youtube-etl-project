import os
from pathlib import Path

import pandas as pd
from googleapiclient.discovery import build

# === CONFIGURATION ===
API_KEY = os.environ.get("YOUTUBE_API_KEY", "").strip()
if not API_KEY:
    raise RuntimeError("Set YOUTUBE_API_KEY to a new, restricted YouTube Data API key.")
CHANNEL_ID = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Example: Google Developers

youtube = build("youtube", "v3", developerKey=API_KEY)

def get_channel_details(channel_id):
    request = youtube.channels().list(
        part="snippet,statistics,contentDetails",
        id=channel_id
    )
    response = request.execute()
    info = response["items"][0]

    return {
        "channel_title": info["snippet"]["title"],
        "subscribers": int(info["statistics"]["subscriberCount"]),
        "views": int(info["statistics"]["viewCount"]),
        "total_videos": int(info["statistics"]["videoCount"]),
        "uploads_playlist_id": info["contentDetails"]["relatedPlaylists"]["uploads"]
    }

def get_videos_from_playlist(playlist_id, max_results=10):
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults=max_results
    )
    response = request.execute()

    videos = []
    for item in response["items"]:
        videos.append({
            "video_id": item["contentDetails"]["videoId"],
            "title": item["snippet"]["title"],
            "published_at": item["contentDetails"]["videoPublishedAt"]
        })
    return videos

if __name__ == "__main__":
    channel = get_channel_details(CHANNEL_ID)
    videos = get_videos_from_playlist(channel["uploads_playlist_id"])
    
    df = pd.DataFrame(videos)
    df["channel_title"] = channel["channel_title"]
    
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    df.to_csv("data/raw/youtube_videos.csv", index=False)
    print("✅ Data saved to data/raw/youtube_videos.csv")
