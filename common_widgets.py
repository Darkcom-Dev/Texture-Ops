import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd

class TexturePreview(tk.LabelFrame):
    def __init__(self, app, text, im_size):
        super().__init__(app, text=text)

        self.im_size = im_size

        self.im = Image.new('RGBA', (self.im_size, self.im_size), (0, 0, 0, 0))
        self.im = self.im.resize((self.im_size, self.im_size))
        self.imtk = ImageTk.PhotoImage(self.im)


        self.path_entry = tk.Entry(self)
        self.path_entry.grid(row=0,column=0,sticky='we')
        self.path_entry.bind("<KeyRelease>", self.on_path_entry_change)

        self.examine_button = tk.Button(self, text='Examine',command=self.load_path)
        self.examine_button.grid(row=0, column=1, sticky='we')

        self.preview = tk.Label(self,text='Futuro logo', image=self.imtk)
        self.preview.grid(row=1,column=0, columnspan=2,sticky='we')

        self.prev_button = tk.Button(self, text='Preview',command=self.load_image)
        self.prev_button.grid(row=2, column=0, columnspan=2, sticky='we')

    def load_image(self):
        self.im = Image.open(self.path_entry.get())
        self.im = self.im.resize((self.im_size, self.im_size))
        self.imtk = ImageTk.PhotoImage(self.im)
        self.preview.configure(image=self.imtk)

    def load_path(self):
        # -defaultextension, -filetypes, -initialdir, -initialfile, -multiple, -parent, -title, or -typevariable
        path = fd.askopenfilename(filetypes=[("PNG Files", "*.png"),("Texture Files", "*.tiff"), ("All Files", "*.*")])
        self.path_entry.insert(0, path)

    def on_path_entry_change(self, event):

        try :
            self.im = Image.open(self.path_entry.get())
            self.im = self.im.resize((self.im_size, self.im_size))
            self.imtk = ImageTk.PhotoImage(self.im)
            self.preview.configure(image=self.imtk)
        except Exception as e:
            print(e)

class SavePath(tk.LabelFrame):
    def __init__(self, app, text, button_text):
        super().__init__(app, text=text)

        self.path_entry = tk.Entry(self)
        self.path_entry.grid(row=0,column=0,sticky='we')
        self.path_entry.bind("<KeyRelease>", self.on_path_entry_change)

        self.examine_button = tk.Button(self, text=button_text,command=self.load_path)
        self.examine_button.grid(row=1, column=0, columnspan=2, sticky='we')

    def load_path(self):
        # -defaultextension, -filetypes, -initialdir, -initialfile, -multiple, -parent, -title, or -typevariable
        path = fd.asksaveasfilename(filetypes=[("Image Files", "*.png;*.jpg;*.tiff"),("PNG Files", "*.png"),("Texture Files", "*.tiff"), ("All Files", "*.*")])
        self.path_entry.insert(0, path)

    def on_path_entry_change(self, event):
        pass