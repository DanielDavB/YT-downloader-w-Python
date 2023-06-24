from pytube import YouTube
from tqdm import tqdm
import os

# Function to download audio from YouTube
def download_audio(url):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Filter for audio streams
        audio_streams = video.streams.filter(only_audio=True)

        # Get the first audio stream
        audio = audio_streams.first()

        # Get the title of the video
        video_title = video.title

        # Define the filename
        filename = f"{video_title}.mp3"

        # Get the file size of the audio stream
        file_size = audio.filesize

        # Define the progress bar
        progress_bar = tqdm(total=file_size, unit='bytes', unit_scale=True)

        # Download the audio stream
        audio.download(filename='audio')

        # Rename the downloaded file to the video title
        os.rename('audio.mp3', filename)

        # Close the progress bar
        progress_bar.close()

        print(f"Audio '{filename}' downloaded successfully!")

    except Exception as e:
        print("Error:", str(e))

# Prompt the user to enter the YouTube URL
youtube_url = input("Enter the YouTube URL: ")

# Call the function to download the audio
download_audio(youtube_url)
