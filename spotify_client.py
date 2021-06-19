import random
import string
import urllib
from warnings import resetwarnings
import requests
from requests.models import Response

class SpotifyClient():
    def __init__(self, api_key):
        self.api_key = api_key

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