import tkinter as tk
from channel_mixer import get_channel_mix
from common_widgets import SaveTexture

class Channel_Mixer_Top(tk.Toplevel):
    def __init__(self, parent, r_path, g_path, b_path, a_path, size_selected):
        super().__init__(parent)
        self.title('Channel Mixer')
        self.geometry('264x312')
        self.resizable(False, False)

        self.r_path = r_path
        self.g_path = g_path
        self.b_path = b_path
        self.a_path = a_path


        self.im = get_channel_mix(self.r_path, 
                             self.g_path, 
                             self.b_path, 
                             self.a_path, 
                             size_selected)
        
        self.im_preview = self.im.resize((256, 256))

        self.preview = SaveTexture(self, 'Channel Mixed Texture', 'Save', self.im_preview, self.im, size_selected)
        self.preview.grid(row=0,column=0,sticky='news')
