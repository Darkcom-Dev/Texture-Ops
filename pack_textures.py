#!/usr/bin/env python3

from PIL import Image
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import argparse

def pack_textures(size:int, routes, save_filename):

    print('Message from pack textures')
    
    result = Image.new('RGBA',[size * 2, size * 2])

    positions = ([0,0],[size,0],[0,size],[size, size])

    for i in range(0,4):
        if routes[i] == '':
            result.paste(Image.new('L',[size,size]),positions[i])
        else:
            result.paste(Image.open(routes[i],'r').resize([size,size]), positions[i])

    result.save(save_filename,'png')
    result.show()

class App():
    def __init__(self, window) -> None:

        self.win = window
        self.win.config(width=800, height=600)
        self.win.title('Texture channel mixer')

        
        # Etiqueta y botones
        instructions = ttk.Label(self.win,text='Este programa combina de 1 a 4 imágenes como un pack')
        instructions.grid(column= 0,row= 0, sticky='WE', columnspan=2)
        instructions1 = ttk.Label(self.win,text='** Se creará una imagen blanca por cada ruta faltante')
        instructions1.grid(column= 0,row= 11, sticky='WE', columnspan=2)

        filetypes = [('texture files',r'*.png *.tif'),('all files','*.*')]
        # Canal R

        r_filename = tk.StringVar()

        r_label = ttk.Label(self.win,text='Primera imagen - superior izquierda')
        r_label.grid(column= 0,row= 1, sticky='WE')
        r_entry = ttk.Entry(self.win, textvariable=r_filename)
        r_entry.grid(column= 0, row= 2, sticky='WE',padx= 5,columnspan=2)
        r_button = ttk.Button(self.win,text='Examine',command= lambda: r_filename.set(askopenfilename(filetypes= filetypes)))
        r_button.grid(column= 2, row= 2)
        
        # Canal G
        g_filename = tk.StringVar()
        g_label = ttk.Label(self.win,text='Segunda imagen - superior derecha')
        g_label.grid(column= 0, row= 3, sticky='WE')
        g_entry = ttk.Entry(self.win,textvariable=g_filename)
        g_entry.grid(column= 0, row= 4, sticky='WE',padx= 5, columnspan=2)
        g_button = ttk.Button(self.win, text='Examine',command=lambda: g_filename.set(askopenfilename(filetypes=filetypes)))
        g_button.grid(column= 2, row= 4)
        
        # Canal B
        b_filename = tk.StringVar()
        b_label = ttk.Label(self.win,text='Tercera imagen - inferior izquierda')
        b_label.grid(column= 0, row= 5, sticky='WE')
        b_entry = ttk.Entry(self.win, textvariable=b_filename)
        b_entry.grid(column= 0, row= 6, sticky='WE',padx= 5, columnspan=2)
        b_button = ttk.Button(self.win, text='Examine',command=lambda: b_filename.set(askopenfilename(filetypes=filetypes)))
        b_button.grid(column= 2, row= 6)
        
        # Canal A
        a_filename = tk.StringVar()
        a_label = ttk.Label(self.win,text='Cuarta imagen - inferior derecha')
        a_label.grid(column= 0, row= 7, sticky='WE')
        a_entry = ttk.Entry(self.win, textvariable=a_filename)
        a_entry.grid(column= 0, row= 8, sticky='WE',padx= 5, columnspan=2)
        a_button = ttk.Button(self.win, text='Examine',command=lambda: a_filename.set(askopenfilename(filetypes=filetypes)))
        a_button.grid(column= 2, row= 8)
        
        # Aplicacion
        apply_label = ttk.Label(self.win,text='Ruta y nombre del nuevo archivo resultante y tamaño')
        apply_label.grid(column= 0, row= 9, sticky='WE')
        apply_entry = ttk.Entry(self.win)
        apply_entry.grid(column= 0, row= 10, sticky='WE',padx= 5)
        sizes = [256,512,1024,2048,4096]
        size_drop = tk.Spinbox(self.win, values= sizes)
        size_drop.grid(column= 1, row= 10)
        apply_button = ttk.Button(self.win, text='Aplicar',command=lambda:pack_textures(int(size_drop.get()),[r_filename.get(),g_filename.get(),b_filename.get(),a_filename.get()],apply_entry.get())) # .save(f'{apply_entry.getvar()}.png', 'png')
        apply_button.grid(column= 2, row= 10)

def main():
    # Ventana
    root = tk.Tk()
    application = App(root)
    root.mainloop()

parser = argparse.ArgumentParser('Texture Atlas packer')

if __name__ == '__main__':

    parser.add_argument('--size',type=int)
    parser.add_argument('--path',nargs='+',type=str)
    parser.add_argument('--name',type=str)
    args = parser.parse_args()
    if args.size:
        pack_textures(args.size,args.path,args.name)
    else:
        main()
    
    

