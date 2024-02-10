import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image, ImageTk
from channel_mixer import get_channel_mix

class Channel_Mixer_Top(tk.Toplevel):
    def __init__(self, parent, r_path, g_path, b_path, a_path, size_selected):
        super().__init__(parent)
        self.title('Channel Mixer')

        self.settings_group = tk.LabelFrame(self, text='Ajustes')
        self.settings_group.grid(row=0,column=0,sticky='news')

        self.preview_lf = tk.LabelFrame(self, text='Previsualización')
        self.preview_lf.grid(row=0,column=1,sticky='news')

        self.intro_label = tk.Label(self.settings_group, text='Este programa combina 3 0 4 texturas en escala de grises para componer una nueva textura RGBA')
        self.intro_label.grid(row=0,column=0,columnspan=2,sticky='we')
        
        self.r_path = r_path
        self.g_path = g_path
        self.b_path = b_path
        self.a_path = a_path


        self.warning_label = tk.Label(self.settings_group, text='** Se creará un canal blanco por cada textura faltante')
        self.warning_label.grid(row=25, column=0, sticky='we')
        self.size_options = size_selected

        self.im = get_channel_mix(self.r_path, 
                             self.g_path, 
                             self.b_path, 
                             self.a_path, 
                             256)

        self.imtk = ImageTk.PhotoImage(self.im)
        self.image_preview = tk.Label(self.preview_lf, image=self.imtk)
        self.image_preview.grid(row=0,column=0, columnspan=2,sticky='we')

        self.path_button = tk.Button(self.preview_lf, text='Save',command=self.save_texture)
        self.path_button.grid(row=21, column=0, columnspan=2, sticky='we')


    def save_texture(self):
        save_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[("Image Files", "*.png;*.jpg;*.tiff"),("PNG Files", "*.png"),("Texture Files", "*.tiff"), ("All Files", "*.*")])
        im = get_channel_mix(self.r_path,
                             self.g_path,
                             self.b_path,
                             self.a_path,
                             int(self.size_options))
        im.save(save_path)
        messagebox.showinfo('Texture Saved', f'Generated {save_path} Texture Image Saved!')
        

    def preview(self):
        im = get_channel_mix(self.r_path, 
                             self.g_path, 
                             self.b_path, 
                             self.a_path, 
                             256)
        im = im.resize((256, 256))
        self.imtk = ImageTk.PhotoImage(im)
        self.image_preview['image'] = self.imtk