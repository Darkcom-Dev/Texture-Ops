import tkinter as tk
from channel_mixer import get_channel_split
from common_widgets import SaveTexture

class Channel_Splitter(tk.Toplevel):

    def __init__(self, parent, path, size_selected):
        super().__init__(parent)
        self.title('Channel Splitter')
        self.geometry('524x648')
        self.resizable(False, False)

        self.im_r, self.im_g, self.im_b, self.im_a = get_channel_split(path, size_selected)

        self.im_r_preview = self.im_r.resize((256, 256))
        self.im_g_preview = self.im_g.resize((256, 256))
        self.im_b_preview = self.im_b.resize((256, 256))
        self.im_a_preview = self.im_a.resize((256, 256))

        self.r_img = SaveTexture(self, 'Red', 'Save Channel R', self.im_r_preview, self.im_r, size_selected)
        self.g_img = SaveTexture(self, 'Green', 'Save Channel G', self.im_g_preview, self.im_g, size_selected)
        self.b_img = SaveTexture(self, 'Blue', 'Save Channel B', self.im_b_preview, self.im_b, size_selected)
        self.a_img = SaveTexture(self, 'Alpha', 'Save Channel A', self.im_a_preview, self.im_a, size_selected)

        self.r_img.grid(row=0, column=0, sticky='news')
        self.g_img.grid(row=0, column=1, sticky='news')
        self.b_img.grid(row=1, column=0, sticky='news')
        self.a_img.grid(row=1, column=1, sticky='news')

        self.intro_label = tk.Label(self, text='Este programa separa un canal de una textura RGBA')
        self.intro_label.grid(row=2,column=0,columnspan=3,sticky='we')

    