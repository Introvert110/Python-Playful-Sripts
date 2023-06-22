from pytube import Playlist

# Provide the URL of the YouTube playlist
playlist_url = input("Enter the URL of the YouTube playlist: ")

# Create a Playlist object
playlist = Playlist(playlist_url)

# Iterate over the videos in the playlist
for video in playlist.videos:
    print(f"Downloading: {video.title}")
    video.streams.get_highest_resolution().download()
    print("Download completed!")

print("All videos in the playlist have been downloaded.")
