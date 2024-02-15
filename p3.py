from hotel import hotel_view
from tkinter import *

root = Tk()
root.geometry("300x300")

view = (hotel_view[2]*4+'\n')*4
l = Label(root, text=view).pack()

root.mainloop()