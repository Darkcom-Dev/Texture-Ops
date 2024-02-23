import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import channel_mixer_top as cmt
import channel_splitter_top as cst
import flowmap_top as ft
import atlas_top as att
import normalmap_top as nmt
import normalmap_greyscale_top as ngt
import about_top as at

import simplex_top as st
import white_noise_top as wnt
import worley_noise_top as wot
import mandelbrot_top as mbt
import gaussian_noise_top as gnt
import gradient_top as gt

import default_filters_top as dft
import blur_top as bt

import color3dlut_top as c3lt #import color3dlut_top as c3lgbt
import statistics_operations_filter_top as soft
import unsharp_mask_top as umt
import kernel_top as kt
import rank_filter_top as rft
from common_widgets import TexturePreview

class SingletonCommand:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonCommand, cls).__new__(cls)
            print('Esto es singleton')
        return cls._instance

def disable_menu_commands(trigger = False, menus = []):
    
    switch_submenu_commands(menus[0], ['Normalmap', 'Normalmap Greyscale', 'Channel Splitter', 'Channel Mixer', 'Flowmap', 'Atlas Texture'], trigger)
    switch_submenu_commands(menus[1], ['Default Filters', 'Blur', 'Kernel Filter', 'Rank Filter', 'Statistics Filter', 'Unsharp Mask'], trigger)


def switch_submenu_commands(menu,submenus=[], trigger = False):
    for submenu in submenus:
        menu.entryconfig(submenu, state= 'normal' if trigger else 'disabled')


def main():
    app = tk.Tk()
    app.title ('Texture utils')
    app.geometry('512x700')
    app.resizable(False, False)
    style = ttk.Style()

    menu = tk.Menu(app)
    app.config(menu=menu)
    menu['background'] = '#1E1E1E'
    menu['foreground'] = 'white'
    menu_app = tk.Menu(menu)
    menu_help = tk.Menu(menu)
    menu_generate = tk.Menu(menu)
    menu_filters = tk.Menu(menu)
    # ------------------------------------------------------------------
    menu.add_cascade(label='Generate', menu=menu_generate)
    menu.add_cascade(label='Textures', menu=menu_app, command=disable_menu_commands)
    menu.add_cascade(label='Filters', menu=menu_filters)
    menu.add_cascade(label='Help', menu=menu_help)
    # ------------------------------------------------------------------
    menu_help.add_command(label='About', command=lambda: at.About_Top(app))
    menu_help['background'] = '#1E1E1E'
    menu_help['foreground'] = 'white'
    # ------------------------------------------------------------------

    menu_app.add_command(label='Channel Mixer', command=lambda: cmt.Channel_Mixer_Top(app, texture_A.path_entry.get(), texture_B.path_entry.get(), texture_C.path_entry.get(), texture_D.path_entry.get(), size_selected.get()))
    menu_app.add_command(label='Atlas Texture', command=lambda: att.Atlas_Texture_Top(app, texture_A.path_entry.get(), texture_B.path_entry.get(), texture_C.path_entry.get(), texture_D.path_entry.get(), size_selected.get()))
    menu_app.add_command(label='Flowmap', command=lambda: ft.Flowmap_Top(app, texture_A.path_entry.get(), size_selected.get()))
    menu_app.add_command(label='Channel Splitter', command=lambda: cst.Channel_Splitter(app, texture_A.path_entry.get(), size_selected.get()))
    menu_app.add_command(label='Normalmap', command=lambda: nmt.Normalmap_Top(app, texture_A.path_entry.get(), size_selected.get()))
    menu_app.add_command(label='Normalmap Greyscale', command=lambda: ngt.Normalmap_Greyscale_Top(app, texture_A.path_entry.get(), size_selected.get()))
    menu_app['background'] = '#1E1E1E'
    menu_app['foreground'] = 'white'
    # ------------------------------------------------------------------
    menu_generate['background'] = '#1E1E1E'
    menu_generate['foreground'] = 'white'
    menu_generate.add_command(label='Simplex Noise', command=lambda: st.Simplex_Top(app, size_selected.get()))
    menu_generate.add_command(label='White Noise', command=lambda: wnt.WhiteNoiseTop(app, size_selected.get()))
    menu_generate.add_command(label='Worley Noise', command=lambda: wot.WorleyNoiseTop(app, size_selected.get()))
    menu_generate.add_command(label='Mandelbrot', command=lambda: mbt.MandelbrotTop(app, size_selected.get()))
    menu_generate.add_command(label='Gaussian Noise', command=lambda: gnt.GaussinaNoiseTop(app, size_selected.get()))
    menu_generate.add_command(label='Gradient', command=lambda: gt.GradientTop(app, size_selected.get()))
    # ------------------------------------------------------------------
    menu_filters['background'] = '#1E1E1E'
    menu_filters['foreground'] = 'white'
    menu_filters.add_command(label='Default Filters', command=lambda: dft.DefaultFiltersTop(app, texture_A.path_entry.get(), size_selected.get()))
    menu_filters.add_command(label='Blur', command=lambda: bt.BlurTop(app, texture_A.path_entry.get(), size_selected.get()))

    menu_filters.add_command(label='Unsharp Mask', command=lambda: umt.UnsharpMaskTop(app, texture_A.path_entry.get(), size_selected.get()))
    menu_filters.add_command(label='Kernel Filter', command=lambda: kt.KernelTop(app, texture_A.path_entry.get(), size_selected.get()))
    menu_filters.add_command(label='Rank Filter', command=lambda: rft.RankFilterTop(app, texture_A.path_entry.get(), size_selected.get()))
    menu_filters.add_command(label='Statistics Filter', command=lambda: soft.StatisticsOperationsFilterTop(app, texture_A.path_entry.get(), size_selected.get()))
    menu_filters.add_command(label='Color3DLUT', command=lambda: c3lt.Color3DLUTTop(app, texture_A.path_entry.get(), size_selected.get()))
    menu_filters.entryconfig('Color3DLUT', state='disabled')
    # -----------------------------------------------------------------
    
    disable_menu_commands(False, [menu_app, menu_filters])

    texture_A = TexturePreview(app, 'Texture A', 240)
    texture_A.grid(row=0,column=0,sticky='news')
    
    texture_B = TexturePreview(app, 'Texture B', 240)
    texture_B.grid(row=0,column=1,sticky='news')
    
    texture_C = TexturePreview(app, 'Texture C', 240)
    texture_C.grid(row=1,column=0,sticky='news')
    
    texture_D = TexturePreview(app, 'Texture D', 240)
    texture_D.grid(row=1,column=1,sticky='news')

    texture_A.is_valid_file.trace_add('write', lambda *args: disable_menu_commands(texture_A.is_valid_file.get(), [menu_app, menu_filters]))
    
    size_selected = tk.IntVar()
    size_list = [256, 512, 1024, 2048, 4096]
    size_options_menu = tk.OptionMenu(app, size_selected, *size_list)
    size_selected.set(256)
    size_options_menu.grid(row=2, column=0, sticky='we')

    
    app.mainloop()
    print('Esto es main')



if __name__ == '__main__':
    main()
