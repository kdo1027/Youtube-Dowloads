from pytube import YouTube
from sys import argv

# Get the video url from the command line
link = argv[1]
yt = YouTube(link)

# Get the video info
print("Title: ", yt.title)
print("View: ", yt.views)

# Get the highest resolution
yd = yt.streams.get_highest_resolution()

# Download the vid
yd.download('Users/khanhdo/Downloads')