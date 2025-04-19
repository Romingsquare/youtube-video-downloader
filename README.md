# YouTube Shorts Downloader

A simple Python tool to download YouTube shorts videos using yt-dlp.

## Features

- Download multiple YouTube shorts videos in batches
- Resume downloads from where they left off
- Error handling and automatic retries
- High quality video downloads

## Requirements

- Python 3.6+
- yt-dlp
- numpy (optional)

## Installation

1. Clone this repository:

```
git clone https://github.com/Romingsquare/youtube-video-downloader.git
cd youtube-shorts-downloader
```

2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:

   - Windows: `venv\Scripts\activate.bat`
   - Linux/Mac: `source venv/bin/activate`

4. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

1. Add your YouTube shorts URLs to the `video_urls` list in `youtube_downloader.py`
2. Run the script:

```
python youtube_downloader.py
```

3. To resume downloads after interruption, update the `start_index` value to continue from where you left off

## Configuration

You can customize the download options by modifying the `ydl_opts` dictionary in the script:

```python
ydl_opts = {
    'format': 'best',  # Change to desired format
    'outtmpl': 'downloads/%(title)s.%(ext)s',  # Output path template
    'nooverwrites': True,  # Don't overwrite existing files
    'no_warnings': False,  # Show warnings
    'ignoreerrors': True,  # Continue on errors
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for personal use only. Always respect copyright laws and YouTube's Terms of Service.
