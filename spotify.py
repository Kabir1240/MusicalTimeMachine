import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


KEYS_PATH = "keys.json"


class Spotify:
    def __init__(self):
        # get keys
        with open(KEYS_PATH, 'r') as file:
            keys = json.load(file)["spotify"]
        self.client_id = keys['client_id']
        self.client_secret = keys['client_secret']
  
        # authorization
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                                client_secret=self.client_secret, 
                                                                scope="playlist-modify-private",
                                                                redirect_uri="https://example.com/"))
        
        self.user_id = self.sp.current_user()['id']
    
    def search(self, query:str, limit:int=20):     
        results = self.sp.search(q=query, limit=limit)
        return [track["uri"] for _, track in enumerate(results['tracks']['items'])]

    def create_playlist(self, name):
        return self.sp.user_playlist_create(self.user_id, name, False)
    
    def add_songs_to_playlist(self, playlist_uri, track_uris):
        self.sp.playlist_add_items(playlist_id=playlist_uri, items=track_uris)