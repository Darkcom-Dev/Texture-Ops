import tkinter as tk
from PIL import Image
import normalmap as nm
from common_widgets import SaveTexture

class Normalmap_Greyscale_Top(tk.Toplevel):
    def __init__(self, parent, path, size_selected):
        super().__init__(parent)

        self.parent = parent
        self.title("Normalmap Greyscale Top")
        self.geometry('264x320')
        self.resizable(False, False)

        self.path = path
        self.size = size_selected
        self.im = Image.open(path)
        self.im_grayscale = nm.normalmap_to_grayscale(self.im)
        self.im_grayscale_preview = self.im_grayscale.resize((256, 256))


        self.save_widget = SaveTexture(self, 'Gray Scale Texture', 'Save', self.im_grayscale_preview, self.im_grayscale, self.size)
        self.save_widget.grid(row=6, column=0, columnspan=3, sticky='we')

