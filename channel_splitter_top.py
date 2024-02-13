import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image, ImageTk
from channel_mixer import get_channel_split

class Channel_Splitter(tk.Toplevel):

    def __init__(self, parent, path, size_selected):
        super().__init__(parent)
        self.title('Channel Splitter')
        self.geometry('525x605')
        self.resizable(False, False)

        self.im_r, self.im_g, self.im_b, self.im_a = get_channel_split(path, size_selected)

        self.imtk_r = ImageTk.PhotoImage(self.im_r)
        self.imtk_g = ImageTk.PhotoImage(self.im_g)
        self.imtk_b = ImageTk.PhotoImage(self.im_b)
        self.imtk_a = ImageTk.PhotoImage(self.im_a)

        self.settings_group = tk.LabelFrame(self, text='Ajustes')
        self.settings_group.grid(row=0,column=0,sticky='news')

        self.preview_lf = tk.LabelFrame(self, text='Previsualización')
        self.preview_lf.grid(row=0,column=1,sticky='news')

        
        self.label_im_r = tk.Label(self.preview_lf, image=self.imtk_r)
        self.label_im_r.grid(row=0,column=0,sticky='news')

        self.button_save_r = tk.Button(self.preview_lf, text='Guardar canal R', command=self.save_r)
        self.button_save_r.grid(row=1,column=0,sticky='we')

        self.label_im_g = tk.Label(self.preview_lf, image=self.imtk_g)
        self.label_im_g.grid(row=0,column=1,sticky='news')

        self.button_save_g = tk.Button(self.preview_lf, text='Guardar canal G', command=self.save_g)
        self.button_save_g.grid(row=1,column=1,sticky='we')

        self.label_im_b = tk.Label(self.preview_lf, image=self.imtk_b)
        self.label_im_b.grid(row=5,column=0,sticky='news')

        self.button_save_b = tk.Button(self.preview_lf, text='Guardar canal B', command=self.save_b)
        self.button_save_b.grid(row=6,column=0,sticky='we')

        self.label_im_a = tk.Label(self.preview_lf, image=self.imtk_a)
        self.label_im_a.grid(row=5,column=1,sticky='news')

        self.button_save_a = tk.Button(self.preview_lf, text='Guardar canal A', command=self.save_a)
        self.button_save_a.grid(row=6,column=1,sticky='we')

        self.intro_label = tk.Label(self.settings_group, text='Este programa separa un canal de una textura RGBA')

    def save_r(self):
        filename = fd.asksaveasfilename(filetypes = [('Image files',r'*.png *.tif'),('all files','*.*')], defaultextension=".png")
        if filename:
            self.im_r.save(filename)

    def save_g(self):
        filename = fd.asksaveasfilename(filetypes = [('Image files',r'*.png *.tif'),('all files','*.*')], defaultextension=".png")
        if filename:
            self.im_g.save(filename)

    def save_b(self):
        filename = fd.asksaveasfilename(filetypes = [('Image files',r'*.png *.tif'),('all files','*.*')], defaultextension=".png")
        if filename:
            self.im_b.save(filename)

    def save_a(self):
        filename = fd.asksaveasfilename(filetypes = [('Image files',r'*.png *.tif'),('all files','*.*')], defaultextension=".png")
        if filename:
            self.im_a.save(filename)