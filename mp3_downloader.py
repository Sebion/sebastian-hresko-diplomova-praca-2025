import requests
import re
import os

class MP3Downloader:
    def __init__(self, base_directory="../mp3songs"):
        self.base_directory = base_directory

    def download_mp3(self, preview_url, track_id, playlist_name=None):
        # Ensure playlist name is in valid syntax and replace spaces with underscores
        if playlist_name:
            playlist_name = re.sub(r'\s+', '_', playlist_name)
            directory = f"{self.base_directory}/{playlist_name}"
        else:
            directory = self.base_directory

        # Ensure the directory exists
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Construct destination file path
        dest_file = f"{directory}/{track_id}.mp3"

        # Download the file
        with open(dest_file, "wb") as f:
            response = requests.get(preview_url)
            f.write(response.content)
        return dest_file