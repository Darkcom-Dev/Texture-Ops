import tkinter as tk
from tkinter import filedialog as fd
import channel_mixer_top as cmt
import channel_splitter_top as cst
import flowmap_top as ft
import atlas_top as att
import normalmap_top as nmt
import normalmap_greyscale_top as ngt
import about_top as at
from common_widgets import TexturePreview

class SingletonCommand:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonCommand, cls).__new__(cls)
            print('Esto es singleton')
        return cls._instance



def main():
    app = tk.Tk()
    app.title ('Texture utils')
    app.geometry('512x700')
    app.resizable(False, False)

    menu = tk.Menu(app)
    app.config(menu=menu)
    menu['background'] = '#1E1E1E'
    menu['foreground'] = 'white'
    menu_app = tk.Menu(menu)
    menu_help = tk.Menu(menu)
    menu.add_cascade(label='App', menu=menu_app)
    menu.add_command(label='Help', command=lambda: at.About_Top(app))
    menu_help.add_command(label='About')
    menu_help['background'] = '#1E1E1E'
    menu_help['foreground'] = 'white'
    menu_app.add_command(label='Channel Mixer', command=lambda: cmt.Channel_Mixer_Top(app, texture_A.path_entry.get(), texture_B.path_entry.get(), texture_C.path_entry.get(), texture_D.path_entry.get(), size_selected.get()))
    menu_app.add_command(label='Atlas Texture', command=lambda: att.Atlas_Texture_Top(app, texture_A.path_entry.get(), texture_B.path_entry.get(), texture_C.path_entry.get(), texture_D.path_entry.get(), size_selected.get()))
    menu_app.add_command(label='Flowmap', command=lambda: ft.Flowmap_Top(app, texture_A.path_entry.get(), size_selected.get()))
    menu_app.add_command(label='Channel_Splitter', command=lambda: cst.Channel_Splitter(app, texture_A.path_entry.get(), size_selected.get()))
    menu_app.add_command(label='Normalmap', command=lambda: nmt.Normalmap_Top(app, texture_A.path_entry.get(), size_selected.get()))
    menu_app.add_command(label='Normalmap_Greyscale', command=lambda: ngt.Normalmap_Greyscale_Top(app, texture_A.path_entry.get(), size_selected.get()))
    menu_app['background'] = '#1E1E1E'
    menu_app['foreground'] = 'white'


    texture_A = TexturePreview(app, 'Texture A', 240)
    texture_A.grid(row=0,column=0,sticky='news')
    
    texture_B = TexturePreview(app, 'Texture B', 240)
    texture_B.grid(row=0,column=1,sticky='news')
    
    texture_C = TexturePreview(app, 'Texture C', 240)
    texture_C.grid(row=1,column=0,sticky='news')
    
    texture_D = TexturePreview(app, 'Texture D', 240)
    texture_D.grid(row=1,column=1,sticky='news')
    
    size_selected = tk.IntVar()
    size_list = [256, 512, 1024, 2048, 4096]
    size_options_menu = tk.OptionMenu(app, size_selected, *size_list)
    size_selected.set(256)
    size_options_menu.grid(row=2, column=0, sticky='we')






    
    app.mainloop()
    print('Esto es main')



if __name__ == '__main__':
    main()