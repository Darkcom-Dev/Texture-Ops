import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from common_widgets import SaveTexture

class UnsharpMaskTop(tk.Toplevel):

    def __init__(self, app, path, size_selected):
        super().__init__(app)

        self.path = path
        self.size = size_selected
        self.im = Image.open(self.path)
        self.im = self.im.filter(ImageFilter.UnsharpMask(radius=5, percent=150, threshold=3))

        self.preview = self.im.resize((256, 256))
        self.size = size_selected

        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.gaussian_scale_label = tk.Label(self.settings_lf, text='Radius:')
        self.gaussian_scale_label.grid(row=0, column=0, sticky='e')

        self.gaussian_scale_default = tk.IntVar(value=5)
        self.gaussian_scale = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.gaussian_scale_default, orient='horizontal')
        self.gaussian_scale.grid(row=1, column=0, sticky='we')

        self.percent_scale_label = tk.Label(self.settings_lf, text='Percent:')
        self.percent_scale_label.grid(row=2, column=0, sticky='e')

        self.percent_scale_default = tk.IntVar(value=150)
        self.percent_scale = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.percent_scale_default, orient='horizontal')
        self.percent_scale.grid(row=3, column=0, sticky='we')

        self.threshold_scale_label = tk.Label(self.settings_lf, text='Threshold:')
        self.threshold_scale_label.grid(row=4, column=0, sticky='e')

        self.threshold_scale_default = tk.IntVar(value=3)
        self.threshold_scale = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.threshold_scale_default, orient='horizontal')
        self.threshold_scale.grid(row=5, column=0, sticky='we')
        
        self.blur_button = tk.Button(self.settings_lf, text='Unsharp Mask',command=self.blur)
        self.blur_button.grid(row=6, column=0, columnspan=2, sticky='we')
        
        self.preview_st = SaveTexture(self, 'Blurred Texture', 'Save', self.preview, self.im, self.size)
        self.preview_st.grid(row=0,column=1,sticky='news')



    def blur(self):

        self.im = Image.open(self.path)
        self.im = self.im.filter(ImageFilter.UnsharpMask(radius=self.gaussian_scale_default.get(), percent=self.percent_scale_default.get(), threshold=self.threshold_scale_default.get()))
        self.im_preview = self.im.resize((256, 256))
        self.preview_st.on_update(self.im, self.im_preview, None)
        print('blurring', self.gaussian_scale_default.get())