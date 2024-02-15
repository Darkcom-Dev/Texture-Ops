import tkinter as tk
import atlas
from common_widgets import SaveTexture

class Atlas_Texture_Top(tk.Toplevel):
    def __init__(self, parent, top_left_path, top_right_path, bottom_left_path, bottom_right_path, size_selected):
        super().__init__(parent)
        self.title('Atlas Texture Composer')
        self.geometry('264x312')
        self.resizable(False, False)

        self.tl_path = top_left_path
        self.tr_path = top_right_path
        self.bl_path = bottom_left_path
        self.br_path = bottom_right_path


        self.im = atlas.get_atlas(self.tl_path, 
                                  self.tr_path, 
                                  self.bl_path, 
                                  self.br_path, 
                                  size_selected)
        self.im_preview = self.im.resize((256, 256))

        self.preview = SaveTexture(self, 'Atlas Texture', 'Save', self.im_preview, self.im, size_selected)
        self.preview.grid(row=0,column=0,sticky='news')



