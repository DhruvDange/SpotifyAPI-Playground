import os
from spotify_client import SpotifyClient
playlist_id = "6fb9YXUIyfc9tkJ0Ry3lzT"
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

def run():
    # Create environment variable that contains the Spotify client id
    # used getenv to replace with value
    spotify_client = SpotifyClient(client_id, client_secret)
    random_tracks = spotify_client.get_popular_tracks(85)
    track_uri = [track['uri'] for track in random_tracks]
    
    was_added_to_playlist = spotify_client.add_tracks_to_playlist(track_uri, playlist_id)
    if was_added_to_playlist:
        for track in random_tracks:
            print(f"Added {track['name']}")

if __name__ == '__main__':
    run()