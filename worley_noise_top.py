import tkinter as tk
from common_widgets import SaveTexture
from PIL import Image, ImageTk
from simplex_noise import generate_worley_noise

class WorleyNoiseTop(tk.Toplevel):
    def __init__(self, app, size_selected):
        super().__init__(app)
        self.title = 'Worley Noise'
        self.geometry('375x315')
        self.resizable(False, False)

        self.size = size_selected
        self.im = generate_worley_noise(self.size, self.size, 8, True)
        self.im_preview = self.im.resize((256, 256))

        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.points_scale_label = tk.Label(self.settings_lf, text='Points:')
        self.points_scale_label.grid(row=2, column=0, sticky='e')
        self.points_scale_default = tk.IntVar(value=8)
        self.points_scale = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.points_scale_default, orient='horizontal')
        self.points_scale.grid(row=3, column=0, sticky='we')

        self.if_seamless_default = tk.BooleanVar(value=True)
        self.if_seamless = tk.Checkbutton(self.settings_lf, text='Seamless', variable=self.if_seamless_default)
        self.if_seamless.grid(row=5, column=0, sticky='we')

        self.generate_button = tk.Button(self.settings_lf, text='Generate', command=self.generate)
        self.generate_button.grid(row=6, column=0, sticky='we')

        self.save_widget = SaveTexture(self, 'Worley Noise', 'Save', self.im_preview, self.im, self.size)
        self.save_widget.grid(row=0, column=1, sticky='we')

    def generate(self):
        self.im = generate_worley_noise(self.size, self.size, 
                                        int(self.points_scale_default.get()), 
                                        bool(self.if_seamless_default.get()))
        self.im_preview = self.im.resize((256, 256))
        self.save_widget.on_update(self.im, self.im_preview, None)