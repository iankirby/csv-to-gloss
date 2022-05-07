#!/usr/bin/python3

import tkinter
from tkinter.ttk import Combobox

window=tkinter.Tk()
window.title("csv-to-gloss")

ex=tkinter.Button(window,text="examples file",fg='black')
ex.place(x=10,y=20)

translit=tkinter.Button(window,text="transliteration key",fg='black')
translit.place(x=10, y=50)


# v0=IntVar()
# v0.set(1)
package1=Radiobutton(window,text="linguex",variable=v0, value=1)
package2=Radiobutton(window,text="gb4e", variable=v0, value=2)
package1.place(x=30, y=0)
package2.place(x=40,y=0)

window.geometry("600x400+20+40")


window.mainloop()