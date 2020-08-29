from pytube import YouTube
import json

file = "./playlists.json"
save_dir = "./downloads/"

with open(file) as f:
    data = json.load(f)

for piece in data["arr"]:
    for link in piece["links"]:
        yt = YouTube(link)
        yt.streams.filter(only_audio=True).first().download("downloads/" + piece["dir"])