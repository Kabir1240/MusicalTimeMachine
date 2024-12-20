from tkinter import Label, Entry, Button, Canvas, ttk
from typing import Dict


class TkinterWidgets:
    def __init__(self, label_dict: Dict[str, Label]|None = None, entry_dict: Dict[str, Entry] | None = None,
                 button_dict: Dict[str, Button] | None = None, canvas_dict: Dict[str, Canvas] | None = None):
        """
        allows user to initialize tkinter widgets for their program
        :param label_dict: dictionary of Label objects
        :param entry_dict: dictionary of Entry objects
        :param button_dict: dictionary of button objects
        """

        if label_dict is not None:
            self.label_dict = label_dict
        else:
            self.label_dict = {}

        if entry_dict is not None:
            self.entry_dict = entry_dict
        else:
            self.entry_dict = {}

        if button_dict is not None:
            self.button_dict = button_dict
        else:
            self.button_dict = {}

        if canvas_dict is not None:
            self.canvas_dict = canvas_dict
        else:
            self.canvas_dict = {}
        
        self.progress_bar_dict = {}

    def get_labels(self, key: str | None = None) -> Label | Dict[str, Label]:
        """
        returns Label widgets
        :param key: Key for the label. If none is given, the entire dictionary will be returned
        :return: either a single Label if key is given, otherwise the entire Label dictionary
        """
        if key is not None:
            return self.label_dict[key]
        else:
            return self.label_dict

    def get_entries(self, key: str | None = None) -> Entry | Dict[str, Entry]:
        """
        returns Entry widgets
        :param key: Key for the Entry. If none is given, the entire dictionary will be returned
        :return: either a single Entry if key is given, otherwise the entire Entry dictionary
        """
        if key is not None:
            return self.entry_dict[key]
        else:
            return self.entry_dict

    def get_buttons(self, key: str | None = None) -> Button | Dict[str, Button]:
        """
        returns Button widgets
        :param key: Key for the Button. If none is given, the entire dictionary will be returned
        :return: either a single Button if key is given, otherwise the entire Button dictionary
        """
        if key is not None:
            return self.button_dict[key]
        else:
            return self.button_dict

    def get_canvas(self, key: str | None = None) -> Canvas | Dict[str, Canvas]:
        """
        returns Canvas widgets
        :param key: Key for the Canvas. If none is given, the entire dictionary will be returned
        :return: either a single Canvas if key is given, otherwise the entire Cavas dictionary
        """
        if key is not None:
            return self.canvas_dict[key]
        else:
            return self.canvas_dict
    
    def get_progress_bar(self, key: str | None = None) -> ttk.Progressbar | Dict[str, ttk.Progressbar]:
        """
        returns Progressbar widgets
        :param key: Key for the Progressbar. If none is given, the entire dictionary will be returned
        :return: either a single Progressbar if key is given, otherwise the entire Progressbar dictionary
        """
        
        if key is not None:
            return self.progress_bar_dict[key]
        else:
            return self.progress_bar_dict

    def add_label(self, key: str, label: Label) -> None:
        """
        adds a single Label object to the label dictionary at key position
        :param key: key
        :param label: Label object
        :return: None
        """
        self.label_dict[key] = label

    def add_entry(self, key: str, entry: Entry) -> None:
        """
        adds a single Entry object to the entry dictionary at key position
        :param key: key
        :param entry: Entry object
        :return: None
        """
        self.entry_dict[key] = entry

    def add_button(self, key: str, button: Button) -> None:
        """
        adds a single Button object to the button dictionary at key position
        :param key: key
        :param button: Button object
        :return: None
        """
        self.button_dict[key] = button

    def add_canvas(self, key:str, canvas: Canvas) -> None:
        """
        adds a single Canvas object to the canvas dictionary at key position
        :param key: key
        :param canvas: Canvas object
        :return: None
        """
        self.canvas_dict[key] = canvas
    
    def add_progress_bar(self, key:str, progress_bar: ttk.Progressbar) -> None:
        """
        adds a single Progressbar object to the progress_bar dictionary at key position
        :param key: key
        :param progress_bar: Progressbar object
        :return: None
        """
        self.progress_bar_dict[key] = progress_bar

    def add_label_dict(self, label_dict: Dict[str, Label]) -> None:
        """
        adds all Labels from label_dict to current Label repository
        :param label_dict: a dictionary of Label objects
        :return: None
        """
        for (key, value) in label_dict.items():
            self.label_dict[key] = value

    def add_entry_dict(self, entry_dict: Dict[str, Entry]) -> None:
        """
        adds all entries from entry_dict to current Entry repository
        :param entry_dict: a dictionary of Entry objects
        :return: None
        """
        for (key, value) in entry_dict.items():
            self.entry_dict[key] = value

    def add_button_dict(self, button_dict: Dict[str, Button]) -> None:
        """
        adds all buttons from button_dict to current Button repository
        :param button_dict: a dictionary of Button objects
        :return: None
        """
        for (key, value) in button_dict.items():
            self.button_dict[key] = value

    def add_canvas_dict(self, canvas_dict: Dict[str, Canvas]) -> None:
        """
        adds all canvas' from canvas_dict to current Canvas repository
        :param canvas_dict: a dictionary of Canvas objects
        :return: None
        """
        for (key, value) in canvas_dict.items():
            self.canvas_dict[key] = value

    def add_progress_bar_dict(self, progress_bar_dict: Dict[str, ttk.Progressbar]) -> None:
        """
        adds all Progressbars from progress_bar_dict to current Canvas repository
        :param canvas_dict: a dictionary of progress_bar objects
        :return: None
        """
        for (key, value) in progress_bar_dict.items():
            self.progress_bar_dict_dict[key] = value