#Booking App View by Tahnee Pitter-Duncan | Feb 2024
import openpyxl
import os 
import tkinter
from tkinter import ttk
from tkinter import messagebox
from rich.prompt import Prompt
from rich.console import Console
from BookingController import *
from Views.HotelView import *


# Window Initialized -------------------------------------
window = tkinter.Tk()
window.title("HWB Hotels Booking App")
window.geometry("600x500")
winWidth = window.winfo_width()

# Window Elements
frame = tkinter.Frame(window)
frame.pack()

welcome_frame = tkinter.LabelFrame(frame, text="HWB Hotels")
welcome_frame.grid(row=0, column=0)

booking_frame = tkinter.LabelFrame(frame, text="Booking Form")
booking_frame.grid(row=1, column=0)


# 1st Frame -----------------------------------------------------
welcome_label = tkinter.Label(welcome_frame, text="Welcome to HWB Hotels Booking app!")
welcome_label.grid(row=0, column=0)

welcome_paragraph_label = tkinter.Label(welcome_frame, text="Here are the available rooms we have:")
welcome_paragraph_label.grid(row=1, column=0)

# Hotel Room View
hotel_frame = tkinter.Frame(welcome_frame, width=150, height=100, bd=2, relief="ridge")
hotel_frame.grid(row=2, column=0, pady=20,padx=20)

gf_view_output = tkinter.Label(hotel_frame, text='')
gf_view_output.grid(row=0, column=0)

book_below_label = tkinter.Label(welcome_frame, text= "Fill out the form below to book your stay today!")
book_below_label.grid(row=4, column=0)


# 1st Frame -----------------------------------------------------
booking_label = tkinter.Label(booking_frame, text="Booking Form")
welcome_label.grid(row=0)


# Main ------------------------------------------------------
window.mainloop()