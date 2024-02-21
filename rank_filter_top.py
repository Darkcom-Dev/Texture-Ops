import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from common_widgets import SaveTexture

class RankFilterTop(tk.Toplevel):

    def __init__(self, app, path, size_selected):
        super().__init__(app)

        self.path = path
        self.size = size_selected
        self.im = Image.open(self.path)
        self.im = self.im.filter(ImageFilter.RankFilter(3, 3))
        # blurred_img = img.filter(ImageFilter.GaussianBlur(radius=5))
        self.preview = self.im.resize((256, 256))
        self.size = size_selected
        
        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.size_rank_filter_label = tk.Label(self.settings_lf, text='Size:')
        self.size_rank_filter_label.grid(row=0, column=0, sticky='e')

        self.size_rank_filter_default = tk.IntVar(value=3)
        self.size_rank_filter = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.size_rank_filter_default, orient='horizontal')
        self.size_rank_filter.grid(row=1, column=0, sticky='we')

        self.rank_scale_label = tk.Label(self.settings_lf, text='Rank:')
        self.rank_scale_label.grid(row=2, column=0, sticky='e')

        self.rank_scale_default = tk.IntVar(value=3)
        self.rank_scale = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.rank_scale_default, orient='horizontal')
        self.rank_scale.grid(row=3, column=0, sticky='we')

        self.blur_button = tk.Button(self.settings_lf, text='Rank Filter',command=self.blur)
        self.blur_button.grid(row=4, column=0, sticky='we')
        
        self.preview_st = SaveTexture(self, 'Rank Filter Texture', 'Save', self.preview, self.im, self.size)
        self.preview_st.grid(row=0,column=1,sticky='news')

        

    def blur(self):
        self.im = Image.open(self.path)
        corrected_size = (self.size_rank_filter_default.get() + 1) if (self.size_rank_filter_default.get() % 2 == 0) else self.size_rank_filter_default.get()
        self.im = self.im.filter(ImageFilter.RankFilter(corrected_size, self.rank_scale_default.get()))
        self.preview = self.im.resize((256, 256))

        self.preview_st.on_update(self.im, self.preview, None)
        print('rank filter', corrected_size, self.rank_scale_default.get())

        