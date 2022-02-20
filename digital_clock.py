#digital clock
from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("digital clock")
def clock():
    tick=strftime('%I:%M:%S %p')
    Label.config(text=tick)
    Label.after(1000,clock)

Label=Label(root,font=('ds-digital',90),background='black',foreground='green')
Label.pack(anchor='center')
clock()
mainloop()