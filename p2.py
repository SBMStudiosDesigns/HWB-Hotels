# Practice file for updates I am considering implementing 
#Tahnee Pitter-Duncan


from rich.prompt import Prompt
from rich.console import Console
from hotel import hotel_view
from tkinter import * 

window_root = Tk()

class HWBBookingApp():

    def __init__(self, window_title, window_header):
        super().__init__()
        view = (hotel_view[2]*4+'\n')*4
        self.title('HWB Hotels Booking App')
        self.geometry('800x500') 
        self.window_title = Label(window_root, text="Welcome to HWB Hotels Booking App").pack()
        self.window_header = Label(window_root, text=view).pack()

# Main        
if __name__ == "__main__":
    window_root.mainloop()
    HWBBookingApp()