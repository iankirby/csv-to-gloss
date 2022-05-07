
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


def select_file():
    filetypes=(
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )

    filename=fd.askopenfilename(
        title='Open file',
        ititialdir='.',
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


v0=IntVar()
v0.set(1)
l1=Radiobutton(window,text="linguex",variable=v0,value=1)
l2=Radiobutton(window,text="gb4e",variable=v0, value=2)
l1.place(x=100,y=50)
l2.place(x=180,y=50)




#this runs the application
window.mainloop()