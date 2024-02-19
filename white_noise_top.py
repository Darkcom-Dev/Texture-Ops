import tkinter as tk
from common_widgets import SaveTexture
from PIL import Image, ImageTk
from simplex_noise import generate_white_noise

class WhiteNoiseTop(tk.Toplevel):
    def __init__(self, app, size_selected):
        super().__init__(app)
        self.title = 'White Noise'
        self.geometry('264x370')
        self.resizable(False, False)

        self.size = size_selected
        self.im = generate_white_noise(self.size, self.size)
        self.im_preview = self.im.resize((256, 256))

        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.generate_button = tk.Button(self.settings_lf, text='Generate', command=self.generate)
        self.generate_button.grid(row=0, column=0, sticky='we')

        self.save_widget = SaveTexture(self, 'White Noise', 'Save', self.im_preview, self.im, size_selected)
        self.save_widget.grid(row=6, column=0, sticky='we')

    def generate(self):
        self.im = generate_white_noise(self.size, self.size)
        self.im_preview = self.im.resize((256, 256))
        self.save_widget.on_update(self.im, self.im_preview, None)




        