import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from common_widgets import SaveTexture

class GradientTop(tk.Toplevel):

    def __init__(self, app, size_selected):
        super().__init__(app)

        self.size = size_selected
        self.im = Image.linear_gradient(mode='L')

        self.preview = self.im.resize((256, 256))
        self.size = size_selected
        
        self.title('Gradient')
        # self.geometry('264x320')
        self.resizable(False, False)

        self.setting_lf = tk.LabelFrame(self, text='Settings')
        self.setting_lf.grid(row=0, column=0, sticky='news')

        self.mode_options = ['L', 'P']

        self.mode_var = tk.StringVar(self)
        self.mode_var.set(self.mode_options[0])

        self.mode_menu = tk.OptionMenu(self.setting_lf, self.mode_var, *self.mode_options)
        self.mode_menu.grid(row=0, column=0, sticky='we')

        self.gradient_type_options = ['linear', 'radial']

        self.gradient_type_var = tk.StringVar(self)
        self.gradient_type_var.set(self.gradient_type_options[0])

        self.gradient_type_menu = tk.OptionMenu(self.setting_lf, self.gradient_type_var, *self.gradient_type_options)
        self.gradient_type_menu.grid(row=1, column=0, sticky='we')

        self.update_button = tk.Button(self.setting_lf, text='Update',command=self.blur)
        self.update_button.grid(row=2, column=0, columnspan=2, sticky='we')
        
        self.preview_st = SaveTexture(self, 'Gradient Texture', 'Save', self.preview, self.im, self.size)
        self.preview_st.grid(row=0,column=1,sticky='news')



    def blur(self):
        
        if self.gradient_type_var.get() == 'linear':
            self.im = Image.linear_gradient(mode=self.mode_var.get())
        elif self.gradient_type_var.get() == 'radial':
            self.im = Image.radial_gradient(mode=self.mode_var.get())

        self.preview = self.im.resize((256, 256))
        self.preview_st.on_update(self.im, self.preview, None)