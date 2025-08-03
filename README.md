
# 🎵 Billboard Spotify Time Machine
Create a Spotify playlist from the Billboard Hot 100 chart on any date in history using Python, BeautifulSoup, and the Spotify API. Whether it's the week you were born or a musical throwback from the 2000s, this tool lets you relive the hits with a single command.

<img width="1536" height="1024" alt="f3aaff40-13b1-4714-9399-4162033de7c5" src="https://github.com/user-attachments/assets/189d8a5a-69a7-4600-a9cd-938bac9d20ac" />



---

## 🚀 Features
- Scrapes Billboard Hot 100 chart for any historical date
- Searches and matches songs on Spotify
- Creates a private playlist in your Spotify account
- Handles missing tracks gracefully
- Uses environment variables for secure Spotify authentication

---

## 🧠 Built With
- Python 3.7+  
- `requests` for API communication  
- `BeautifulSoup` for web scraping 
- `spotipy` for Spotify API integration 
- `dotenv` for secure config handling  
- Spotify Developer API + Billboard.com  

---

## 💻 How It Works
1. You enter a date in the format `YYYY-MM-DD`
2. The script fetches that day’s Billboard Hot 100 chart
3. It searches each song on Spotify (with a year filter)
4. Matches are collected and added to a private playlist
5. It prints out the playlist link when done

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/billboard-spotify-time-machine.git
cd billboard-spotify-time-machine
```

### 2. Install Dependencies
```bash
pip install os
pip install requests
pip install import BeautifulSoup
pip install spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
```

### 3. Set Up Spotify Developer Credentials

- Go to: Spotify Developer Dashboard
- Create an app and grab: `CLIENT_ID`, `CLIENT_SECRET` and Add a redirect URI like: `http://123.0.0.1:1234`
- Create an `.env` file
```bash
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://127.0.0.1:9090
```
---

## ▶️ Running the Script
After setting the environment variables, run the script:

```bash
python main.py
```
Follow the prompts, log in to Spotify when asked, and voilà — your playlist is created.

---

## 🌐 APIs Used

| API                | Purpose                              |
|--------------------|--------------------------------------|
| Billboard          | Scrapes song names from Hot 100 chart|
| Spotipy            | Searches songs & creates playlists   |

---

## 🧠 What You’ll Learn
- Web scraping with `BeautifulSoup`.
- Using OAuth with `Spotify`.
- Automating playlist creation
- Handling missing data
- Working with `.env` and secure API credentials

---

## 🙌 Credits
- 👨‍💻 **Built by: Mussa Tariq
- LinkedIn: https://www.linkedin.com/in/mussa-tariq-0652712a0/
- 📊 Billboard.com 
- 🎧 Spotify Developer Team  

---

## 🎧 Final Note
Whether you're feeling nostalgic or want a musical time capsule, this tool brings history to your headphones. From your birth year to the golden age of pop — now it’s just one playlist away.

marvels silently pass above you.

