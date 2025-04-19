import yt_dlp
import os
import time

# Create downloads directory if it doesn't exist
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# List of video URLs
video_urls = [
    "https://www.youtube.com/shorts/url",
    "https://www.youtube.com/url"

  ]

# Start from video 17 (0-based index would be 16)
start_index = 1

# yt-dlp configuration
ydl_opts = {
    'format': 'best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'nooverwrites': True,
    'no_warnings': False,
    'ignoreerrors': True,
}

# Download videos starting from the 17th one
for i, url in enumerate(video_urls[start_index:], start=start_index):
    try:
        print(f"Processing video {i+1}/{len(video_urls)}: {url}")
        
        # Add a delay between requests to avoid rate limiting
        if i > start_index:
            time.sleep(1)
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from {url}...")
            ydl.download([url])
            print(f"Video {i+1} download complete.")
            
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        time.sleep(2)  # Wait a bit longer after an error
        
print("All downloads completed!") 