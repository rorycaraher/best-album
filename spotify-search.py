import sys
import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# user = 

client_credentials_manager = SpotifyClientCredentials(client_id='38ef923dcdc2419fb479849877c46c73', client_secret='05ce1147630843bcb1055f9cced752c5')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

search_album = "Loveless"

results = sp.search(q=search_album,type='album', limit=20)
# user_playlist_create(user, name, public=True, description='')
print(results)
