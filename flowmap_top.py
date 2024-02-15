import tkinter as tk
from flowmap import get_flowmap
from common_widgets import SaveTexture


class Flowmap_Top(tk.Toplevel):
    def __init__(self, parent, path, size_selected):
        super().__init__(parent)
        self.title('Flowmap Creator')
        self.geometry('264x338')
        self.resizable(False, False)

        self.intro_label = tk.Label(self, text='Flowmap basado en Heightmap')
        self.intro_label.grid(row=0,column=0,columnspan=3,sticky='we')

        self.path = path
        self.im = get_flowmap(self.path)
        self.im_preview = self.im.resize((256, 256))

        self.save_widget = SaveTexture(self, 'Flowmap', 'Save', self.im_preview, self.im, size_selected)
        self.save_widget.grid(row=6, column=0, columnspan=3, sticky='we')
