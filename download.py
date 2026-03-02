import urllib.request
import shutil

with urllib.request.urlopen("http://192.168.0.101:1104/MiniDLNA/Music/Till%20It%27s%20Over%20-%20Tristam%20%5BFUknhj30m4g%5D.mp3") as response:
  content_length = response.getheader("Content-Length", 0)
  print(f"Downloading {content_length}B of data...")
  with open("test.mp3", mode="wb") as file:
    shutil.copyfileobj(response, file)
