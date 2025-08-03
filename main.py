import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

# ✏️ Ask user for the date to travel to
DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = DATE.split("-")[0]

# 📃 Request Billboard Hot 100 chart HTML for the given date
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
URL = "https://www.billboard.com/charts/hot-100/"
response = requests.get(f"{URL}{DATE}", headers=HEADER).text
soup = BeautifulSoup(response, 'html.parser')

# 🎵 Extract song titles from the chart page
song_names_spans = soup.select("li ul li h3")
songs_list = [song.getText().strip() for song in song_names_spans]

# 🟢 Spotify API credentials (replace with environment variables)
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REDIRECT_URI = os.environ["REDIRECT_URI"]  # Should match what you registered in the Spotify Developer Dashboard

# 🔐 Authenticate with Spotify using OAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='playlist-modify-private'
    )
)

# 👤 Get current Spotify user's ID
user_id = sp.current_user()['id']

# 📻 Create a private playlist for the selected date
playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)
playlist_id = playlist["id"]

# 🔍 Search each song on Spotify and collect their URIs
uri_list = []
for song in songs_list:
    query = f"track:{song} year:{year}"
    result = sp.search(q=query, type="track", limit=1)
    try:
        track_uri = result['tracks']['items'][0]['uri']
        uri_list.append(track_uri)
    except IndexError:
        print(f"Song not found: {song}")

# ➕ Add found songs to the new playlist
sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
print(f"\n🎉 Playlist created with {len(uri_list)} tracks: https://open.spotify.com/playlist/{playlist_id}")

# This will help you to look at the playlist you made
playlist_url = playlist["external_urls"]["spotify"]
print(f"🎧 View your playlist here: {playlist_url}")


