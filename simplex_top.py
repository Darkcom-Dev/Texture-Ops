import tkinter as tk
from common_widgets import SaveTexture
from PIL import Image, ImageTk
from simplex_noise import generate_seamless_texture


class Simplex_Top(tk.Toplevel):
    def __init__(self, app, size_selected):
        super().__init__(app)
        self.title('Simplex')
        self.geometry('446x336')
        self.resizable(False, False)

        self.settings_lf = tk.LabelFrame(self, text='Settings')
        self.settings_lf.grid(row=0, column=0, sticky='news')

        self.scale_label = tk.Label(self.settings_lf, text='Scale:')
        self.scale_label.grid(row=2, column=0, sticky='e')
        self.scale_default = tk.IntVar(value=50)
        self.scale = tk.Scale(self.settings_lf, from_=1, to=100, variable=self.scale_default, orient='horizontal')
        self.scale.grid(row=3, column=0, sticky='we')

        # self.scale.bind("<Motion>", lambda event: self.update_preview())

        self.octaves_label = tk.Label(self.settings_lf, text='Octaves:')
        self.octaves_label.grid(row=4, column=0, sticky='e')
        self.octaves = tk.Scale(self.settings_lf, from_=1, to=10, orient='horizontal')
        self.octaves.grid(row=5, column=0, sticky='we')

        self.persistence_label = tk.Label(self.settings_lf, text='Persistence:')
        self.persistence_label.grid(row=6, column=0, sticky='e')
        self.persistence_default = tk.DoubleVar(value=0.5)
        self.persistence = tk.Spinbox(self.settings_lf, from_=0.1, to=10.0, textvariable=self.persistence_default, increment=0.1)
        self.persistence.grid(row=7, column=0, sticky='we')

        self.lacunarity_label = tk.Label(self.settings_lf, text='Lacunarity:')
        self.lacunarity_label.grid(row=8, column=0, sticky='e')
        self.lacunarity_default = tk.DoubleVar(value=2.0)
        self.lacunarity = tk.Spinbox(self.settings_lf, from_=1.0, to=10.0, textvariable=self.lacunarity_default, increment=0.1)
        self.lacunarity.grid(row=9, column=0, sticky='we')

        self.seed_label = tk.Label(self.settings_lf, text='Seed:')
        self.seed_label.grid(row=10, column=0, sticky='e')
        self.seed_scale = tk.Scale(self.settings_lf, from_=0, to=100, orient='horizontal')
        self.seed_scale.grid(row=11, column=0, sticky='we')

        self.update_button = tk.Button(self.settings_lf, text='Update', command=self.update_preview)
        self.update_button.grid(row=12, column=0, sticky='we')

        self.size = size_selected
        self.im = generate_seamless_texture(self.size, self.size, int(self.scale.get()), int(self.octaves.get()), float(self.persistence.get()), float(self.lacunarity.get()), int(self.seed_scale.get()))
        self.im_preview = self.im.resize((256, 256))
        self.noise_preview = SaveTexture(self, 'Noise', 'Save', self.im_preview, self.im, self.size)
        self.noise_preview.grid(row=0, column=1, sticky='news')


    def update_preview(self):
        self.size = self.scale.get()
        self.im = generate_seamless_texture(int(self.size), 
                                            int(self.size), 
                                            int(self.scale.get()),
                                            int(self.octaves.get()),
                                            float(self.persistence.get()),
                                            float(self.lacunarity.get()),
                                            int(self.seed_scale.get()))
        self.im_preview = self.im.resize((256, 256))
        self.noise_preview.on_update(self.im, self.im_preview, None)
        print('updating preview', self.scale.get(), self.octaves.get(), self.persistence.get(), self.lacunarity.get(), self.seed_scale.get())
