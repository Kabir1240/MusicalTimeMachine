from billboard_scraper import get_billboard_top_100
from spotify import Spotify
from tkinter_widgets import TkinterWidgets
from tkinter import Tk, Label, Button, Entry, messagebox, ttk
import threading


class MusicalTimeMachineUserInterface:
    
    def __init__(self):
        self.tk_widgets = TkinterWidgets()
        # self.spotify_interface = Spotify()
        self.window = Tk()        
        
        self.window.title("Musical Time Machine")
        self.window.config(padx=20, pady=20)
        self.window.geometry("450x150")
        
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.create_progress_bar()
        
        self.window.mainloop()
        
    def create_labels(self):
        label_1 = Label(text="Enter Date (YYYY-MM-DD)")
        label_2 = Label(text="Ready to Start?", font=("Courier", 20, 'bold'))
        label_1.grid(row=0, column=0)
        label_2.grid(row=1, column=0, pady=10, columnspan=3)
        
        self.tk_widgets.add_label(key="date", label=label_1)
    
    def create_entries(self):
        entry_1 = Entry()
        entry_1["width"] = 20
        entry_1.grid(row=0, column=1, padx=20)
        
        self.tk_widgets.add_entry(key="date", entry=entry_1)
    
    def create_buttons(self):
        button_1 = Button(text="Enter", font=("Courier", 10, 'bold'), command=self.start_machine_thread)
        button_1.grid(row=0, column=2, padx=20)
        
        self.tk_widgets.add_button(key="enter", button=button_1)
    
    def create_progress_bar(self):
        progress_bar_1 = ttk.Progressbar(self.window, orient="horizontal", length=300, mode="determinate")
        progress_bar_1.grid(row=2, column=0, columnspan=3)
        
        progress_bar_1["value"] = 0
    
    def start_machine(self):
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
            
            # create playlist and add tracks
            playlist_uri = spotify.create_playlist(name=date + " Billboard 100")['uri']
            spotify.add_songs_to_playlist(playlist_uri=playlist_uri, track_uris=track_uris)
            
            # inform user when the operation is complete
            messagebox.showinfo("Task Complete", "Check your spotify!")
            self.tk_widgets.get_buttons(key="enter").config(state="normal")

    def start_machine_thread(self):
        self.tk_widgets.get_buttons(key="enter").config(state="disabled")
        threading.Thread(target=self.start_machine).start()
