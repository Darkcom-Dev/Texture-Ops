import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from common_widgets import SaveTexture

class MandelbrotTop(tk.Toplevel):

    def __init__(self, app, size_selected):
        super().__init__(app)

        self.title('Mandelbrot')
        # self.geometry('370x315')
        self.resizable(False, False)

        self.size = size_selected
        self.im = Image.effect_mandelbrot((self.size, self.size), (0.0, 0.0, 1.0, 1.0), 100)

        self.preview = self.im.resize((256, 256))
        self.size = size_selected
        
        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.extent_x0_label = tk.Label(self.settings_lf, text='X0:')
        self.extent_x0_label.grid(row=0, column=0, sticky='e')

        self.extent_x0 = tk.Spinbox(self.settings_lf, from_=-10, to=10, increment=0.1)
        self.extent_x0.grid(row=1, column=0, sticky='we')

        self.extent_y0_label = tk.Label(self.settings_lf, text='Y0:')
        self.extent_y0_label.grid(row=2, column=0, sticky='e')

        self.extent_y0 = tk.Spinbox(self.settings_lf, from_=-10, to=10, increment=0.1)
        self.extent_y0.grid(row=3, column=0, sticky='we')

        self.extent_x1_label = tk.Label(self.settings_lf, text='X1:')
        self.extent_x1_label.grid(row=4, column=0, sticky='e')

        self.extent_x1 = tk.Spinbox(self.settings_lf, from_=-10, to=10, increment=0.1)
        self.extent_x1.grid(row=5, column=0, sticky='we')

        self.extent_y1_label = tk.Label(self.settings_lf, text='Y1:')
        self.extent_y1_label.grid(row=6, column=0, sticky='e')

        self.extent_y1 = tk.Spinbox(self.settings_lf, from_=-10, to=10, increment=0.1)
        self.extent_y1.grid(row=7, column=0, sticky='we')

        self.quality_scale_label = tk.Label(self.settings_lf, text='Quality:')
        self.quality_scale_label.grid(row=8, column=0, sticky='e')

        self.quality_scale_default = tk.IntVar(value=100)
        self.quality_scale = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.quality_scale_default, orient='horizontal')
        self.quality_scale.grid(row=9, column=0, sticky='we')

        self.update_button = tk.Button(self.settings_lf, text='Update',command=self.blur)
        self.update_button.grid(row=10, column=0, sticky='we')
        
        self.preview_st = SaveTexture(self, 'Mandelbrot Texture', 'Save', self.preview, self.im, self.size)
        self.preview_st.grid(row=0,column=1,sticky='news')



    def blur(self):
        
        extent = (
            float(self.extent_x0.get()),
            float(self.extent_y0.get()),
            float(self.extent_x1.get()),
            float(self.extent_y1.get())
        )

        self.im = Image.effect_mandelbrot((self.size, self.size), extent=extent, quality=self.quality_scale_default.get())
        self.preview = self.im.resize((256, 256))
        self.preview_st.on_update(self.im, self.preview, None)