
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

window=tk.Tk()
# var=StringVar()
window.title('csv-to-text')
window.geometry("400x300+10+10")

#Button for selecting exmaple file.

def select_file():
    filetypes=(
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )

    filename=fd.askopenfilename(
        title='Open file',
        ititialdir='./',
        filetypes=filetypes)
    showinfo(
        title='Select a file',
        message=filename
    )


open_examples=ttk.Button(
    window,
    text='Select examples',
    command=select_file
)

open_examples.pack(expand=True)
open_examples.place(x=50,y=20)

def select_transliteration():
    filetypes=(
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )

    filename=fd.askopenfilename(
        title='Open file',
        initialdir='.',
        filetypes=filetypes
    )
    showinfo(
        title='Select a file',
        message=filename
    )
    
open_translit=ttk.Button(
    window,
    text='Select transliteration file',
    command=select_transliteration
)

open_translit.pack(expand=True)

def select_glossing_key():
    filetypes=(
        ('Text files', '*.txt'),
        ('All files','*.*')
    )
    filename=fd.askopenfile(
        title='Open glossing file',
        initialdir='.',
        filetypes=filetypes
    )
    showinfo(
        title='Select a file',
        message=filename
    )



open_glossing=ttk.Button(
    window,
    text='Select glossing file',
    command=select_glossing_key
)

open_glossing.pack(expand=True)


v0=IntVar()
v0.set(1)
l1=Radiobutton(window,text="linguex",variable=v0,value=1)
l2=Radiobutton(window,text="gb4e",variable=v0, value=2)
l1.place(x=150,y=100)
l2.place(x=2040,y=100)




#this runs the application
window.mainloop()