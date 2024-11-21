from billboard_scraper import get_billboard_top_100
from spotify import Spotify
from tkinter_widgets import TkinterWidgets
from tkinter import Tk, Label, Button, Entry, messagebox, ttk
import threading


class MusicalTimeMachineUserInterface:
    
    def __init__(self):
        """
        • Asks user for a date
        • scrapes billboard top 100 for top 100 songs on that date
        • Creates a playlist and adds all the songs to it
        • Handles that functionality and the user interface
        """
        
        # creates a data structure to keep tk inter widgets
        self.tk_widgets = TkinterWidgets()
        
        # create and configure window
        self.window = Tk()        
        
        self.window.title("Musical Time Machine")
        self.window.config(padx=20, pady=20)
        self.window.geometry("450x150")
        
        # create widgets
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.create_progress_bar()
        
        # handle window main loop
        self.window.mainloop()
        
    def create_labels(self):
        """
        create labels and stores them
        """
        label_1 = Label(text="Enter Date (YYYY-MM-DD)")
        label_2 = Label(text="Ready to Start?", font=("Courier", 20, 'bold'))
        label_1.grid(row=0, column=0)
        label_2.grid(row=1, column=0, pady=10, columnspan=3)
        
        label_dict = {
            "date": label_1,
            "status": label_2,
        }
        
        self.tk_widgets.add_label_dict(label_dict=label_dict)
    
    def create_entries(self):
        """
        create entries and stores them
        """
        
        entry_1 = Entry()
        entry_1["width"] = 20
        entry_1.grid(row=0, column=1, padx=20)
        
        self.tk_widgets.add_entry(key="date", entry=entry_1)
    
    def create_buttons(self):
        """
        create buttons and stores them
        """
        
        button_1 = Button(text="Enter", font=("Courier", 10, 'bold'), command=self.start_machine_thread)
        button_1.grid(row=0, column=2, padx=20)
        
        self.tk_widgets.add_button(key="enter", button=button_1)
    
    def create_progress_bar(self):
        """
        create progress bars and stores them
        """
        
        progress_bar_1 = ttk.Progressbar(self.window, orient="horizontal", length=300, mode="determinate")
        progress_bar_1.grid(row=2, column=0, columnspan=3)
        
        progress_bar_1["value"] = 0
        
        self.tk_widgets.add_progress_bar(key="status", progress_bar=progress_bar_1)
    
    def update_status(self, current_step: str, percentage: int):
        """
        updates user about the status on the tkinter window

        :param current_step: current step being carried out by program (egs: Finding songs)
        :type current_step: str
        :param percentage: percentage of program progress completed
        :type percentage: int
        """
        
        status_label = self.tk_widgets.get_labels(key="status")
        status_bar = self.tk_widgets.get_progress_bar(key="status")
        
        status_label.config(text=current_step)
        status_bar['value'] = percentage    
    
    def start_machine(self):
        """
        carries out main functionality of the musical time machine.
        • Asks user for a date
        • scrapes billboard top 100 for top 100 songs on that date
        • Creates a playlist and adds all the songs to it
        • updates user about the progress as it does the above
        """
        
        # get date from user
        date = self.tk_widgets.get_entries(key="date").get()
        
        self.update_status(current_step=f"Retrieving track names...", percentage=5)    
        # get billboard top 100 songs
        tracks, artists = get_billboard_top_100(date=date)
        spotify = Spotify()
        
        self.update_status(current_step="Searching for songs...", percentage=25)
        # search for tracks
        track_uris = []
        for track_index in range(len(tracks)):
            query = f"track: {tracks[track_index]} artist: {artists[track_index]}"
            track_uris += spotify.search(query=query, limit=1)
        
        self.update_status(current_step=f"Creating playlist...", percentage=50)
        # create playlist and add tracks
        playlist_uri = spotify.create_playlist(name=f"{date} Billboard 100")['uri']
        
        self.update_status(current_step="Adding tracks...", percentage=75)
        spotify.add_songs_to_playlist(playlist_uri=playlist_uri, track_uris=track_uris)
        self.update_status(current_step="", percentage=20)
        
        self.update_status(current_step="Done!", percentage=100)
        # inform user when the operation is complete
        messagebox.showinfo("Task Complete", "Check your spotify!")
        self.tk_widgets.get_buttons(key="enter").config(state="normal")

    def start_machine_thread(self):
        """
        disables the enter button and starts the main function on a separate thread to prevent the window from freezing
        """
        
        self.tk_widgets.get_buttons(key="enter").config(state="disabled")
        threading.Thread(target=self.start_machine).start()
