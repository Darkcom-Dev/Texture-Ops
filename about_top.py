import tkinter as tk


class About_Top(tk.Toplevel):
    def __init__(self, app):
        super().__init__(app)
        self.title('About')
        self.geometry('300x100')
        self.resizable(False, False)
        # self.overrideredirect(True)
        # self.attributes('-topmost', True)

        self.version_label = tk.Label(self, text='Version 0.1.0')
        self.version_label.grid(row=0, column=0, sticky='we')

        self.created_by_label = tk.Label(self, text='Created by: Braulio León Madrid Escobar')
        self.created_by_label.grid(row=1, column=0, sticky='we')