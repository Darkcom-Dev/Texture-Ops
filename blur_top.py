import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from common_widgets import SaveTexture

class BlurTop(tk.Toplevel):

    def __init__(self, app, path, size_selected):
        super().__init__(app)

        self.title('Blur')
        self.geometry('408x316')
        self.resizable(False, False)

        self.path = path
        self.size = size_selected
        self.im = Image.open(self.path)
        self.im = self.im.filter(ImageFilter.GaussianBlur(radius=5))
        self.preview = self.im.resize((256, 256))
        self.size = size_selected
        
        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.options_blur = ['Box Blur', 'Gaussian Blur']
        self.option_blur_var = tk.StringVar(self)
        self.option_blur_var.set(self.options_blur[0])
        self.option_blur_menu = tk.OptionMenu(self.settings_lf, self.option_blur_var, *self.options_blur)
        self.option_blur_menu.grid(row=0, column=0, sticky='we')

        self.radius_scale_label = tk.Label(self.settings_lf, text='Radius:')
        self.radius_scale_label.grid(row=1, column=0, sticky='e')
        self.radius_scale_default = tk.IntVar(value=5)
        self.radius_scale = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.radius_scale_default, orient='horizontal')
        self.radius_scale.grid(row=2, column=0, sticky='we')

        self.blur_button = tk.Button(self.settings_lf, text='Update Blur',command=self.update_blur)
        self.blur_button.grid(row=3, column=0, columnspan=2, sticky='we')

        self.preview_st = SaveTexture(self, 'Blurred Texture', 'Save', self.preview, self.im, self.size)
        self.preview_st.grid(row=0,column=1,sticky='news')



    def update_blur(self):
        
        self.im = Image.open(self.path)
        if self.option_blur_var.get() == 'Box Blur':
            self.im = self.im.filter(ImageFilter.BoxBlur(radius=self.radius_scale_default.get()))
        elif self.option_blur_var.get() == 'Gaussian Blur':
            self.im = self.im.filter(ImageFilter.GaussianBlur(radius=self.radius_scale_default.get()))
        self.preview = self.im.resize((256, 256))
        self.preview_st.on_update(self.im, self.preview, None)