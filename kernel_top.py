import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from common_widgets import SaveTexture

class KernelTop(tk.Toplevel):

    def __init__(self, app, path, size_selected):
        super().__init__(app)

        self.title('Kernel 3x3')
        self.geometry('800x316')
        self.resizable(False, False)

        self.path = path
        self.size = size_selected
        self.im = Image.open(self.path)
        self.kernel = ImageFilter.Kernel((3, 3), (0.25, 0.5, 0.75, 10, -1, 21, -0.75, -0.5, 0.333))
        self.im = self.im.filter(self.kernel)
        # blurred_img = img.filter(ImageFilter.GaussianBlur(radius=5))
        self.preview = self.im.resize((256, 256))
        self.size = size_selected
        
        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.kernel_label = tk.Label(self.settings_lf, text='Kernel:')
        self.kernel_label.grid(row=0, column=0, sticky='e')

        self.k_0_Spinbox = tk.Spinbox(self.settings_lf, from_=-100, to=100, increment=0.1)
        self.k_0_Spinbox.grid(row=1, column=0, sticky='e')
        self.k_0_Spinbox.delete(0, 'end')
        self.k_0_Spinbox.insert(0, 1)

        self.k_1_Spinbox = tk.Spinbox(self.settings_lf, from_=-100, to=100, increment=0.1)
        self.k_1_Spinbox.grid(row=1, column=1, sticky='e')
        self.k_1_Spinbox.delete(0, 'end')
        self.k_1_Spinbox.insert(0, 1)

        self.k_2_Spinbox = tk.Spinbox(self.settings_lf, from_=-100, to=100, increment=0.1)
        self.k_2_Spinbox.grid(row=1, column=2, sticky='e')
        self.k_2_Spinbox.delete(0, 'end')
        self.k_2_Spinbox.insert(0, 1)

        self.k_3_Spinbox = tk.Spinbox(self.settings_lf, from_=-100, to=100, increment=0.1)
        self.k_3_Spinbox.grid(row=2, column=0, sticky='e')
        self.k_3_Spinbox.delete(0, 'end')
        self.k_3_Spinbox.insert(0, 1)

        self.k_4_Spinbox = tk.Spinbox(self.settings_lf, from_=-100, to=100, increment=0.1)
        self.k_4_Spinbox.grid(row=2, column=1, sticky='e')
        self.k_4_Spinbox.delete(0, 'end')
        self.k_4_Spinbox.insert(0, 1)

        self.k_5_Spinbox = tk.Spinbox(self.settings_lf, from_=-100, to=100, increment=0.1)
        self.k_5_Spinbox.grid(row=2, column=2, sticky='e')
        self.k_5_Spinbox.delete(0, 'end')
        self.k_5_Spinbox.insert(0, 1)

        self.k_6_Spinbox = tk.Spinbox(self.settings_lf, from_=-100, to=100, increment=0.1)
        self.k_6_Spinbox.grid(row=3, column=0, sticky='e')
        self.k_6_Spinbox.delete(0, 'end')
        self.k_6_Spinbox.insert(0, 1)

        self.k_7_Spinbox = tk.Spinbox(self.settings_lf, from_=-100, to=100, increment=0.1)
        self.k_7_Spinbox.grid(row=3, column=1, sticky='e')
        self.k_7_Spinbox.delete(0, 'end')
        self.k_7_Spinbox.insert(0, 1)

        self.k_8_Spinbox = tk.Spinbox(self.settings_lf, from_=-100, to=100, increment=0.1)
        self.k_8_Spinbox.grid(row=3, column=2, sticky='e')
        self.k_8_Spinbox.delete(0, 'end')
        self.k_8_Spinbox.insert(0, 1)

        self.blur_button = tk.Button(self.settings_lf, text='Apply Kernel',command=self.apply_kernel)
        self.blur_button.grid(row=5, column=0, columnspan=3, sticky='we')
        
        self.preview_st = SaveTexture(self, 'Kernel Texture', 'Save', self.preview, self.im, self.size)
        self.preview_st.grid(row=0,column=1,sticky='news')



    def apply_kernel(self):
        
        self.im = Image.open(self.path)
        self.im = self.im.filter(self.kernel)
        kernel = [float(self.k_0_Spinbox.get()), float(self.k_1_Spinbox.get()), float(self.k_2_Spinbox.get()),
                  float(self.k_3_Spinbox.get()), float(self.k_4_Spinbox.get()), float(self.k_5_Spinbox.get()),
                  float(self.k_6_Spinbox.get()), float(self.k_7_Spinbox.get()), float(self.k_8_Spinbox.get())]
        self.im = self.im.filter(ImageFilter.Kernel((3, 3), kernel))
        self.preview = self.im.resize((256, 256))
        self.preview_st.on_update(self.im, self.preview, None)
        print(kernel, type(kernel[0]))

        '''
        ## Suavizado de imagen por kernel
        [1,1,1,1,1,1,1,1,1]

        ## Sharpness de imagen por kernel
        [1,-2,1,-2,5,-2,1,-2,1]
        [0, -1, 0, -1, 5, -1, 0, -1, 0]

        ## Deteccion de bordes de imagen por kernel
        [-1,-1,-1,-1,8,-1,-1,-1,-1]

        ## 
        '''