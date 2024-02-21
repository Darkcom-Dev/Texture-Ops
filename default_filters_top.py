import tkinter as tk
from PIL import Image, ImageFilter
from common_widgets import SaveTexture

class DefaultFiltersTop(tk.Toplevel):

    def __init__(self, app, path, size_selected):
        super().__init__(app)

        self.title('Default Filters')
        self.geometry('440x312')
        self.resizable(False, False)

        self.path = path
        self.size = size_selected
        self.im = Image.open(self.path)
        self.im = self.im.filter(ImageFilter.BLUR)
        # blurred_img = img.filter(ImageFilter.GaussianBlur(radius=5))
        self.preview = self.im.resize((256, 256))
        self.size = size_selected

        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.filter_options = ['Blur', 'Contour', 'Detail', 'Edge Enhance', 'Edge Enhance More', 'Emboss', 'Find Edges', 'Sharpen', 'Smooth', 'Smooth More']
        

        self.filter_var = tk.StringVar(self)
        self.filter_var.set(self.filter_options[0])

        self.filter_menu = tk.OptionMenu(self.settings_lf, self.filter_var, *self.filter_options)
        self.filter_menu.grid(row=0, column=0, sticky='we')
        
        self.blur_button = tk.Button(self.settings_lf, text='Update Filter',command=self.update_filter)
        self.blur_button.grid(row=1, column=0, columnspan=2, sticky='we')

        self.preview_st = SaveTexture(self, 'Blurred Texture', 'Save', self.preview, self.im, self.size)
        self.preview_st.grid(row=0,column=1,sticky='news')

        

    def update_filter(self):
        
        self.im = Image.open(self.path)
        if self.filter_var.get() == 'Blur':
            self.im = self.im.filter(ImageFilter.BLUR)
        elif self.filter_var.get() == 'Contour':
            self.im = self.im.filter(ImageFilter.CONTOUR)
        elif self.filter_var.get() == 'Detail':
            self.im = self.im.filter(ImageFilter.DETAIL)
        elif self.filter_var.get() == 'Edge Enhance':
            self.im = self.im.filter(ImageFilter.EDGE_ENHANCE)
        elif self.filter_var.get() == 'Edge Enhance More':
            self.im = self.im.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif self.filter_var.get() == 'Emboss':
            self.im = self.im.filter(ImageFilter.EMBOSS)
        elif self.filter_var.get() == 'Find Edges':
            self.im = self.im.filter(ImageFilter.FIND_EDGES)
        elif self.filter_var.get() == 'Sharpen':
            self.im = self.im.filter(ImageFilter.SHARPEN)
        elif self.filter_var.get() == 'Smooth':
            self.im = self.im.filter(ImageFilter.SMOOTH)
        elif self.filter_var.get() == 'Smooth More':
            self.im = self.im.filter(ImageFilter.SMOOTH_MORE)

        self.preview = self.im.resize((256, 256))

        self.preview_st.on_update(self.im, self.preview, None)