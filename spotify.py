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
    
    def search(self, query:str, limit:int=20) -> list[str]:
        """
        searches for songs using spotify API, returns a list of track URIs

        :param query: query to search for. You can use this format "track: {track} artist{artist}" along with others
        :type query: str
        :param limit: limit the number of tracks that can be returned, defaults to 20
        :type limit: int, optional
        :return: list of track URIs
        :rtype: list[str]
        """
        results = self.sp.search(q=query, limit=limit)
        return [track["uri"] for _, track in enumerate(results['tracks']['items'])]

    def create_playlist(self, name:str) -> str:
        """
        creates a private playlist for the current user

        :param name: name of playlist
        :type name: str
        :return: URI of playlist
        :rtype: str
        """
        return self.sp.user_playlist_create(self.user_id, name, False)
    
    def add_songs_to_playlist(self, playlist_uri:str, track_uris:list[str]) -> None:
        """
        adds multiple tracks to a spotify playlist

        :param playlist_uri: URI of playlist to add tracks to
        :type playlist_uri: str
        :param track_uris: list of track URIs
        :type track_uris: list[str]
        """
        self.sp.playlist_add_items(playlist_id=playlist_uri, items=track_uris)