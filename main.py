from billboard_scraper import get_billboard_top_100
from spotify import Spotify


def main() -> None:
    """
    Asks user to enter a date. Scrapes songs from billboard top 100 on that date. Adds those songs to a spotify playlist.
    """
    
    # get date from user
    date = input("Which date do you want to be transported to? (YYYY-MM-DD)")
    
    # get billboard top 100 songs
    tracks, artists = get_billboard_top_100(date=date)

    spotify = Spotify()    
    # search for tracks
    track_uris = []
    for track_index in range(len(tracks)):
        query = f"track: {tracks[track_index]} artist: {artists[track_index]}"
        track_uris += spotify.search(query=query, limit=1)
    
    # create playlist and add tracks
    playlist_uri = spotify.create_playlist(name=date + " Billboard 100")['uri']
    spotify.add_songs_to_playlist(playlist_uri=playlist_uri, track_uris=track_uris)
