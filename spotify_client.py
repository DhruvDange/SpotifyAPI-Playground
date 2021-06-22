import random
import string
import urllib
import base64
import os
from urllib.parse import quote
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
            user-library-read"""


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
        self.api_key = spotify_auth.get_access_token()["access_token"]

    
    def get_id(self, uri):
        if "artist" in uri:
            return uri.removeprefix("spotify:artist:")
        elif "track" in uri:
            return uri.removeprefix("spotify:track")



    def get_random_tracks(self):
        url = f'https://api.spotify.com/v1/search'
        wildcard = f'{random.choice(string.ascii_lowercase)}'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(1,2000)
        payload = {
            "q": query,
            "offset": offset,
            "market": "US",
            "type": "track",
            "limit": 2
        }
        response = requests.get(
            url,
            params = payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )
        response_json = response.json()
        tracks = [tracks for tracks in response_json['tracks']['items']]
        print(f"Found {len(tracks)} tracks.")
        print(response_json)
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
        url = f"https://api.spotify.com/v1/search"
        pop_tracks = []

        while(len(pop_tracks)<=20):
            
            wildcard = f'{random.choice(string.ascii_lowercase)}'
            query = urllib.parse.quote(wildcard)
            offset = random.randint(0,1000)
            payload = {
                "q": query,
                "offset": offset,
                "market": "US",
                "type": "track",
                "limit": 20
            }
            response = requests.get(
                url,
                params = payload,
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

    
    def get_artist_uri(self, artist_name):
        query = artist_name
        item_type = "artist"
        url = "https://api.spotify.com/v1/search"
        payload = {
            "q": query,
            "type": item_type
        }
        header = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.get(url, params = payload, headers = header)
        response_json = response.json()
        artists = [artist for artist in response_json['artists']['items']]

        keys = range(1, len(artists)+1)
        values = []
        for artist in artists:
            name = artist["name"]
            followers = artist["followers"]["total"]
            values.append(f"{name}, followers: {followers}")
        artist_names = dict(zip(keys, values))
        for key, value in artist_names.items():
            print(f"{key}: {value}")
        print("Enter number corresponding to artist: ")
        artist_index = int(input("")) - 1
        selected_artist = artists[artist_index]["uri"]
        
        return(self.get_id(selected_artist))




