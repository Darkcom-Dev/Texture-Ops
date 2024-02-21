import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from common_widgets import SaveTexture

class Color3DLUTTop(tk.Toplevel):

    def __init__(self, app, path, size_selected):
        super().__init__(app)

        self.path = path
        self.size = size_selected
        self.im = Image.open(self.path)
        self.lut = [
            ((0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0)),

            ((0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0)),
            
            ((0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0),
            (0.0, 0.0, 0.0), (0.25, 0.25, 0.25), (0.5, 0.5, 0.5), (0.75, 0.75, 0.75), (1.0, 1.0, 1.0)),


        ]   
        self.im = self.im.filter(ImageFilter.Color3DLUT(size=5, table=self.lut))

        self.preview = self.im.resize((256, 256))
        self.size = size_selected

        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.gaussian_scale_label = tk.Label(self.settings_lf, text='Radius:')
        self.gaussian_scale_label.grid(row=0, column=0, sticky='e')

        self.gaussian_scale_default = tk.IntVar(value=5)
        self.gaussian_scale = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.gaussian_scale_default, orient='horizontal')
        self.gaussian_scale.grid(row=1, column=0, sticky='we')
        
        self.blur_button = tk.Button(self.settings_lf, text='Blur',command=self.blur)
        self.blur_button.grid(row=2, column=0, columnspan=2, sticky='we')
        
        self.preview_st = SaveTexture(self, 'Blurred Texture', 'Save', self.preview, self.im, self.size)
        self.preview_st.grid(row=0,column=1,sticky='news')



    def blur(self):

        self.im = Image.open(self.path)
        self.im = self.im.filter(ImageFilter.GaussianBlur(radius=self.gaussian_scale_default.get()))
        self.im_preview = self.im.resize((256, 256))
        self.preview_st.on_update(self.im, self.im_preview, None)
        print('blurring', self.gaussian_scale_default.get())