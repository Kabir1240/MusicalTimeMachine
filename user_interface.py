from billboard_scraper import get_billboard_top_100
from spotify import Spotify
from tkinter_widgets import TkinterWidgets
from tkinter import Tk, Label, Button, Entry


class MusicalTimeMachineUserInterface:
    
    def __init__(self):
        self.tk_widgets = TkinterWidgets()
        # self.spotify_interface = Spotify()
        window = Tk()
        
        
        window.title("Musical Time Machine")
        window.config(padx=20, pady=20)
        
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        
        window.mainloop()
        
    def create_labels(self):
        label_1 = Label(text="Enter Date (YYYY-MM-DD)")
        label_2 = Label(text="Ready?")
        label_1.grid(row=0, column=0)
        label_2.grid(row=1, column=0)
        
        label_dictionary = {
            "date": label_1,
            "update": label_2,
        }
        
        self.tk_widgets.add_label_dict(label_dict=label_dictionary)
    
    def create_entries(self):
        entry_1 = Entry()
        entry_1["width"] = 20
        entry_1.grid(row=0, column=1, padx=20)
        
        self.tk_widgets.add_entry(key="date", entry=entry_1)
    
    def create_buttons(self):
        button_1 = Button(text="Enter", font=("Courier", 10, 'bold'), command=self.start_machine)
        button_1.grid(row=0, column=2, padx=20)
        
        self.tk_widgets.add_button(key="enter", button=button_1)
    
    def start_machine(self):
            update_label = self.tk_widgets.get_labels(key="update")
            
            # get date from user
            date = self.tk_widgets.get_entries(key="date").get()
                        
            # get billboard top 100 songs
            tracks, artists = get_billboard_top_100(date=date)
            spotify = Spotify()
            
            # search for tracks
            track_uris = []
            for track_index in range(len(tracks)):
                query = f"track: {tracks[track_index]} artist: {artists[track_index]}"
                track_uris += spotify.search(query=query, limit=1)
            
            # create playlist
            playlist_uri = spotify.create_playlist(name=date + " Billboard 100")['uri']
            # add tracks
            spotify.add_songs_to_playlist(playlist_uri=playlist_uri, track_uris=track_uris)
            
            update_label.config(text="Done! Go check out your spotify!")
