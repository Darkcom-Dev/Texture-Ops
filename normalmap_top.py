import tkinter as tk
from PIL import Image
import normalmap as nm
from common_widgets import SaveTexture

class Normalmap_Top(tk.Toplevel):
    def __init__(self, parent, path, size_selected):
        super().__init__(parent)

        self.parent = parent
        self.title("Normalmap Top")
        self.geometry('260x312')
        self.resizable(False, False)

        self.path = path
        self.im = Image.open(self.path).convert("L")
        self.size = size_selected
        self.im_normal = nm.grayscale_to_normalmap(self.im)
        self.im_normal_preview = self.im_normal.resize((256, 256))

        self.save_widget = SaveTexture(self, 'Normalmap', 'Save', self.im_normal_preview, self.im_normal, size_selected)
        self.save_widget.grid(row=6, column=0, columnspan=3, sticky='we')


        
