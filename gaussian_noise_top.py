import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from common_widgets import SaveTexture

class GaussinaNoiseTop(tk.Toplevel):

    def __init__(self, app, size_selected):
        super().__init__(app)

        self.size = size_selected
        self.im = Image.effect_noise((self.size, self.size), 50)

        self.preview = self.im.resize((256, 256))
        self.size = size_selected
        
        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.sigma_scale_label = tk.Label(self.settings_lf, text='Sigma:')
        self.sigma_scale_label.grid(row=0, column=0, sticky='e')

        self.sigma_scale_default = tk.IntVar(value=0)
        self.sigma_scale = tk.Scale(self.settings_lf, from_= -100, to=100, variable=self.sigma_scale_default, orient='horizontal')
        self.sigma_scale.grid(row=1, column=0, sticky='we')

        self.blur_button = tk.Button(self.settings_lf, text='Update',command=self.blur)
        self.blur_button.grid(row=2, column=0, columnspan=2, sticky='we')
        
        self.preview_st = SaveTexture(self, 'Gausian Noise Texture', 'Save', self.preview, self.im, self.size)
        self.preview_st.grid(row=0,column=1,sticky='news')

        

    def blur(self):
        
        self.im = Image.effect_noise((self.size, self.size), self.sigma_scale_default.get())
        self.preview = self.im.resize((256, 256))
        self.preview_st.on_update(self.im, self.preview, None)