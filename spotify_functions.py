import spotipy
from spotipy.oauth2 import SpotifyOAuth

#User info
SPOTIPY_CLIENT_ID = 'spotify api client id goes here'
SPOTIPY_CLIENT_SECRET = 'spotify client secret goes here'
SPOTIPY_REDIRECT_URI = 'https://placeholder.github.io/'

#define scope
scope = "user-read-private user-read-playback-state user-modify-playback-state"

#Create Spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=scope))

#Gets connected users Spotify username
def get_user():
    user_values = sp.current_user()
    username = user_values["uri"].replace("spotify:user:", "")
    return username

#Adjusts volume at a given % value 0-100
def adjust_volume(vol_percent):
    sp.volume(vol_percent)

#Grabs users playback status to determine wheather to play or pause music
def play_pause():
    playback_info = sp.current_playback()
    playing = playback_info['is_playing']

    if(playing):
        sp.pause_playback()
    elif(not playing):
        sp.start_playback()

#Skips to the next song queued up
def next_song():
    sp.next_track()

#Goes back to the previous song
def prev_song():
    sp.previous_track()