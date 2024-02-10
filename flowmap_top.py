import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image, ImageTk
from flowmap import get_flowmap
from common_widgets import SavePath


class Flowmap_Top(tk.Toplevel):
    def __init__(self, parent, path, size_selected):
        super().__init__(parent)
        self.title('Flowmap Creator')
        self.geometry('340x392')
        self.resizable(False, False)

        self.intro_label = tk.Label(self, text='Flowmap basado en Heightmap o Grayscale')
        self.intro_label.grid(row=0,column=0,columnspan=3,sticky='we')

        self.path = path
        self.im = get_flowmap(self.path)
        self.im = self.im.resize((256, 256))
        self.imtk = ImageTk.PhotoImage(self.im)

        self.image_preview = tk.Label(self, image=self.imtk)
        self.image_preview.grid(row=3,column=0,columnspan=3,sticky='we')

        self.save_button = tk.Button(self, text='Save',command=self.save)
        self.save_button.grid(row=5, column=2, sticky='we')

    def path(self):
        path = fd.askopenfilename()
        self.path_entry.insert(0, path)

        im = get_flowmap(path)
        im = im.resize((256, 256))
        self.imtk = ImageTk.PhotoImage(im)
        self.image_preview['image'] = self.imtk

    def save(self):
        save_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[("Image Files", "*.png;*.jpg;*.tiff"),("PNG Files", "*.png"),("Texture Files", "*.tiff"), ("All Files", "*.*")])
        im = get_flowmap(self.path)
        im = im.resize((int(self.save_options_size_str), int(self.save_options_size_str)))
        im.save(save_path)

        messagebox.showinfo('Flowmap Saved', f'Generated {save_path} Flowmap Image Saved!')