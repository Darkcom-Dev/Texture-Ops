import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image, ImageTk
import atlas

class Atlas_Texture_Top(tk.Toplevel):
    def __init__(self, parent, top_left_path, top_right_path, bottom_left_path, bottom_right_path, size_selected):
        super().__init__(parent)
        self.title('Atlas Texture Composer')
        self.geometry('678x336')
        self.resizable(False, False)


        self.labeled_group = tk.LabelFrame(self, text='Ajustes')
        self.labeled_group.grid(row=0,column=0,sticky='news')

        self.preview_lf = tk.LabelFrame(self, text='Previsualización')
        self.preview_lf.grid(row=0,column=1,sticky='news')

        self.intro_label = tk.Label(self.labeled_group, text='Este programa combina 4 texturas en una nueva textura RGBA')
        self.intro_label.grid(row=0,column=0,columnspan=4,sticky='we')

        self.tl_path = top_left_path
        self.tr_path = top_right_path
        self.bl_path = bottom_left_path
        self.br_path = bottom_right_path


        
        self.prev_size_options = size_selected


        self.im = atlas.get_atlas(self.tl_path, 
                                  self.tr_path, 
                                  self.bl_path, 
                                  self.br_path, 
                                  256)
        self.imtk = ImageTk.PhotoImage(self.im)

        self.image_label = tk.Label(self.preview_lf, image=self.imtk)
        self.image_label.grid(row=0,column=0, sticky='e')

        self.save_button = tk.Button(self.preview_lf, text='Save',command=self.save)
        self.save_button.grid(row=1, column=0,  sticky='we')


    def save(self):
        save_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[("Image Files", "*.png;*.jpg;*.tiff"),("PNG Files", "*.png"),("Texture Files", "*.tiff"), ("All Files", "*.*")])
        im = atlas.get_atlas(self.tl_path,
                                  self.tr_path,
                                  self.bl_path,
                                  self.br_path,
                                  int(self.prev_size_options))
        im.save(save_path)
        messagebox.showinfo('Atlas Saved', f'Generated {save_path} Atlas Image Saved!')

    def preview(self):
        im = atlas.get_atlas(self.tl_path, 
                                  self.tr_path, 
                                  self.bl_path, 
                                  self.br_path, 
                                  256)
        self.imtk = ImageTk.PhotoImage(im)
        self.image_label['image'] = self.imtk