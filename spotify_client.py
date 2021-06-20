import random
import string
import urllib
import base64
import os
from warnings import resetwarnings
import requests
from requests.models import Response
# Using spotipy library for user authenticationa and OAuth key
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

scope = """ user-read-recently-played, user-top-read, user-read-playback-position,
            app-remote-control, streaming, playlist-read-private, playlist-read-collaborative,
            playlist-modify-public, playlist-modify-private, user-library-modify, 
            user-library-read """


class SpotifyClient():
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        spotify_auth = spotipy.oauth2.SpotifyOAuth(
            client_id=f"{self.client_id}", 
            client_secret=f"{self.client_secret}",
            redirect_uri="http://localhost:8000",
            scope=scope,
            cache_handler=None
        )
        ss =spotify_auth.get_access_token()
        print(ss)
        # self.api_key = st.get_access_token()["access_token"]
        

    def get_random_tracks(self):
        wildcard = f'{random.choice(string.ascii_lowercase)}'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(1,2000)

        url = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track'

        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )
        response_json = response.json()
        tracks = [tracks for tracks in response_json['tracks']['items']]
        print(f"Found {len(tracks)} tracks.")
        return tracks


    def add_tracks_to_playlist(self, track_uris, playlist_id):
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
        response =  requests.put(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            },
            json={
                'uris': track_uris
            }
        )

        return response.ok


    def get_popular_tracks(self, popularity):
        market = "US"
        pop_tracks = []

        while(len(pop_tracks)<=20):
            wildcard = f'{random.choice(string.ascii_lowercase)}'
            query = urllib.parse.quote(wildcard)
            offset = random.randint(0,1000)
            url = f"https://api.spotify.com/v1/search?q={query}&offset={offset}&market={market}&type=track&limit=5"
            response = requests.get(
                url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content_type": "application/json"
                }
            )
            response_json = response.json()
            tracks = [tracks for tracks in response_json['tracks']['items']]
            for track in tracks:
                if (track["popularity"] >= popularity):
                    pop_tracks.append(track)
        return pop_tracks

