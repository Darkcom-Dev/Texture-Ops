import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from common_widgets import SaveTexture

class StatisticsOperationsFilterTop(tk.Toplevel):

    def __init__(self, app, path, size_selected):
        super().__init__(app)

        self.title('Statistics Operations Filter')
        self.geometry('400x312')
        self.resizable(False, False)

        self.path = path
        self.size = size_selected
        self.im = Image.open(self.path)
        self.im = self.im.filter(ImageFilter.MedianFilter(size=5))

        self.preview = self.im.resize((256, 256))
        self.size = size_selected

        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.options_filter = ['Min Filter', 'Median Filter', 'Max Filter', 'Mode Filter']
        self.options_filter_default = tk.StringVar()
        self.options_filter_default.set(self.options_filter[1])
        self.options_filter_menu = tk.OptionMenu(self.settings_lf, self.options_filter_default, *self.options_filter)
        self.options_filter_menu.grid(row=0, column=0, sticky='we')

        self.size_scale_label = tk.Label(self.settings_lf, text='Size:')
        self.size_scale_label.grid(row=1, column=0, sticky='e')

        self.size_scale_default = tk.IntVar(value=5)
        self.size_scale = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.size_scale_default, orient='horizontal')
        self.size_scale.grid(row=2, column=0, sticky='we')
        
        self.blur_button = tk.Button(self.settings_lf, text='Apply Filter',command=self.update_filter)
        self.blur_button.grid(row=5, column=0, columnspan=2, sticky='we')
        
        self.preview_st = SaveTexture(self, 'Statistics Filter Texture', 'Save', self.preview, self.im, self.size)
        self.preview_st.grid(row=0,column=1,sticky='news')



    def update_filter(self):

        self.im = Image.open(self.path)
        corrected_size = self.size_scale_default.get() +1 if (self.size_scale_default.get() % 2 == 0) else self.size_scale_default.get()
        if self.options_filter_default.get() == 'Min Filter':
            self.im = self.im.filter(ImageFilter.MinFilter(size=corrected_size))
        elif self.options_filter_default.get() == 'Median Filter':
            self.im = self.im.filter(ImageFilter.MedianFilter(size=corrected_size))
        elif self.options_filter_default.get() == 'Max Filter':
            self.im = self.im.filter(ImageFilter.MaxFilter(size=corrected_size))
        elif self.options_filter_default.get() == 'Mode Filter':
            self.im = self.im.filter(ImageFilter.ModeFilter(size=corrected_size))
        self.im_preview = self.im.resize((256, 256))
        self.preview_st.on_update(self.im, self.im_preview, None)
        print(self.options_filter_default.get(), self.size_scale_default.get())