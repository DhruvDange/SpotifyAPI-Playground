import os
from spotify_client import SpotifyClient
client_auth = "BQDqTKoJmsn2xcrnm1db639qlSTlSWUEOV-RgSoBrSxrx7marr1GU45sl5nNQ6uq-n-07Y5qGgBazAIelvPB68-JML6gKgbKcP-pr_0nu6r_c0QICMeRa_ucgva0wFqq3z2JEO0Ep4YVr-25Xc403ac7AEozvQETFHpMjijY"
playlist_id = "6fb9YXUIyfc9tkJ0Ry3lzT"

def run():
    # Create environment variable that contains the Spotify client id
    # used getenv to replace with value
    spotify_client = SpotifyClient(client_auth)
    random_tracks = spotify_client.get_random_tracks()
    track_uri = [track['uri'] for track in random_tracks]
    
    was_added_to_playlist = spotify_client.add_tracks_to_playlist(track_uri, playlist_id)
    if was_added_to_playlist:
        for track in random_tracks:
            print(f"Added {track['name']}")

if __name__ == '__main__':
    run()