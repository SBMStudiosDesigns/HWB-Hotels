import getpass
import PySimpleGUI as sg
import customtkinter as ctk
import tkinter as tk
from tkinter import Tk, Label, Button, StringVar, font, messagebox, Menu, Menubutton, OptionMenu
from tkcalendar import Calendar, DateEntry


# Styling
# BUTTON_CONF_1 = {'height' : 1, 'width': 25, 'bg' : '#0d0d0d', 'fg' : "#ffffff"}
# BUTTON_SIZE_VIEW = {'height' : 1, 'width': 20}
# PAD_PACK_OPTIONS = {'padx' : 12, 'pady' : 12}
# PAD_PACK_OPTIONS_NP = {'padx' : 10, 'pady' : 10}
# PAD_PACK_OPTIONS_PLOT = {'padx' : 10, 'pady' : 15}
# PAD_PACK_OPTIONS_VIEW = {'padx' : 5, 'pady' : 4}
# PAD_OPTIONS = {'padx' : 25, 'pady' : 8, 'sticky' : 'W'}
# PAD_OPTIONS_2 = {'padx' : 10, 'pady' : 8, 'sticky' : 'W'}
# PAD_OPTIONS_3 = {'padx' : 5, 'pady' : 5, 'sticky' : 'W'}
# PAD_OPTIONS_4 = {'padx' : 3, 'pady' : 3, 'sticky' : 'W'}
# PAD_OPTIONS_5 = {'padx' : 5, 'pady' : 10, 'sticky' : 'W'}
# PAD_OPTIONS_6 = {'padx' : 5, 'pady' : 15, 'sticky' : 'W'}


userName = '%s!'%(getpass.getuser().capitalize())
main_bgc = "#8AA7A9"
# Utility
def about():
    messagebox.showinfo('About', "This is a sample Booking Application made by Tahnee Pitter-Duncan. \n\nThis app is made using Python and Tkinter. The Tkinter package is used to build a simple GUI.")




class BookingApp(ctk.CTk):

    def __init__(self):
        ctk.CTk.__init__(self)
        self.title("HWB Hotels Booking App")
        self.geometry("600x450")
        
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        ## Initialize Frames
        self.frames = {}
        self.HomePage = HomePage
        self.AccountProfile = AccountProfile
        self.NewBooking = NewBooking
        self.LogIn = LogIn

        ## Defining Frames and Packing it
        for F in {HomePage, NewBooking, AccountProfile, LogIn}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")    
           
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = frame.create_menubar(self)
        self.configure(menu=menubar)
        frame.tkraise()        ## This line will put the frame on front


#---------------------------------------- HOME PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, container):
        super().__init__(container)
        #self.configure(bg="#8AA7A9")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1 )
        self.columnconfigure(0, weight=1)


        # Page Elements
        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=0, column=0, padx=0, pady=0)
        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.grid(row=1, column=0, padx=0, pady=0)

        title_font = ctk.CTkFont(family="Times", size=30)
        heading_font = ctk.CTkFont(family="Times", size=20)
        body_font = ctk.CTkFont(family="Times", size=15)


        hp_label = ctk.CTkLabel(top_frame, text="Home Page", font=title_font)
        # label.pack(pady=0,padx=0)
        hp_label.grid(row=0, column=0, pady=10,padx=0)

        welcome_message = "Welcome to HWB Hotels Booking App " + userName + '!'
        self.welcome_label = ctk.CTkLabel(top_frame,text=welcome_message,font=heading_font)
        # self.welcome.pack(side="top", anchor="center")
        self.welcome_label.grid(row=1, column=0, pady=0,padx=0)

        hp_blurb = "Experience the essence of luxury in the heart of Toronto at our boutique hotel.\nSecure your urban sanctuary today and immerse yourself in the vibrant energy\nof the city. Located in the bustling metropolis of Toronto, our boutique gem\npromises an unforgettable stay."
        self.hp_blurb_label = ctk.CTkLabel(top_frame,text=hp_blurb, font=body_font)
        # self.welcome.pack(side="top", anchor="center")
        self.hp_blurb_label.grid(row=2, column=0, pady=0,padx=0)

        hp_button_label_msg = "Elevate your travel experience – reserve your spot today!"
        self.hp_button_label = ctk.CTkLabel(bottom_frame,text=hp_button_label_msg,font=heading_font)
        # self.welcome.pack(side="top", anchor="center")
        self.hp_button_label.grid(row=0, columnspan=3, sticky='news', pady=5,padx=0)

        new_booking_btn = ctk.CTkButton(bottom_frame, text="New Booking", command=lambda: parent.show_frame(parent.NewBooking))
        new_booking_btn.grid(row=1, column=0,  padx=20, pady=10)

        create_btn = ctk.CTkButton(bottom_frame, text="Create an Account", command=lambda: parent.show_frame(parent.AccountProfile))
        create_btn.grid(row=1, column=1,padx=20, pady=10)

        login_btn = ctk.CTkButton(bottom_frame, text="Login", command=lambda: parent.show_frame(parent.LogIn))
        login_btn.grid(row=1, column=2,padx=20, pady=10)

        

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief="raised", activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief='raised', activebackground="#026AA9")
        menubar.add_cascade(label="Options", menu=filemenu)
        filemenu.add_command(label="New Booking", command=lambda: parent.show_frame(parent.NewBooking))
        filemenu.add_command(label="Account Profile", command=lambda: parent.show_frame(parent.AccountProfile))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=about)
        help_menu.add_separator()

        return menubar


#---------------------------------------- New Booking PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class NewBooking(ctk.CTkFrame):
    def __init__(self, parent, container):
        super().__init__(container)
        #self.configure(bg="#8AA7A9")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        title_font = ctk.CTkFont(family="Times", size=30)
        heading_font = ctk.CTkFont(family="Times", size=20)
        body_font = ctk.CTkFont(family="Times", size=15)

        # Page Elements
        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=0, column=0, sticky='w', padx=15)
        scroll_frame = ctk.CTkFrame(self)
        scroll_frame.grid(row=1, column=0)

        label = ctk.CTkLabel(top_frame, text="New Booking", font=title_font)
        label.grid(row=0, column=0, columnspan=3, sticky='nw', pady=0,padx=0)

        booking_msg = "Fill out the form below to book your stay with us!"
        self.booking_label = ctk.CTkLabel(top_frame,text=booking_msg, font=body_font)
        self.booking_label.grid(row=1, columnspan=3, sticky='nw', pady=0,padx=0)

        booking_scrollbar = ctk.CTkScrollableFrame(
            scroll_frame,
            width=530,
            height=200,
            label_text="Booking Form",
            #label_fg_color="blue",
            #label_text_color="yellow",
            label_font=heading_font,
            label_anchor = "center", # "w",  # n, ne, e, se, s, sw, w, nw, center
            border_width=3,
            border_color="black",
            #fg_color="red",
            scrollbar_fg_color="light gray",
            scrollbar_button_color="gray",
            scrollbar_button_hover_color = "black",
            corner_radius = 10,)
        booking_scrollbar.grid(row = 0, column = 0)

        fname_label = ctk.CTkLabel(booking_scrollbar, text='First Name')
        fname_label.grid(row=0, column=0, sticky='e', padx=10, pady=5)
        fname_entry = ctk.CTkEntry(booking_scrollbar)
        fname_entry.grid(row=0, column=1, padx=5, pady=5)

        lname_label = ctk.CTkLabel(booking_scrollbar, text='Last Name')
        lname_label.grid(row=0, column=2, sticky='e', padx=10, pady=5)
        lname_entry = ctk.CTkEntry(booking_scrollbar)
        lname_entry.grid(row=0, column=3, padx=5, pady=5)

        phone_num_label = ctk.CTkLabel(booking_scrollbar, text='Phone Number')
        phone_num_label.grid(row=1, column=0, sticky='e', padx=10, pady=5)
        phone_num_entry = ctk.CTkEntry(booking_scrollbar)
        phone_num_entry.grid(row=1, column=1, padx=5, pady=5)

        email_label = ctk.CTkLabel(booking_scrollbar, text='Email')
        email_label.grid(row=1, column=2, sticky='e', padx=10, pady=5)
        email_entry = ctk.CTkEntry(booking_scrollbar)
        email_entry.grid(row=1, column=3, padx=5, pady=5)

        start_cal_label = ctk.CTkLabel(booking_scrollbar, text='Check-In')
        start_cal_label.grid(row=2, column=0, sticky='e', padx=10, pady=5)
        # start_cal = Calendar(
        #     booking_scrollbar,
        #     selectmode='day', 
        #     font=body_font,
        #     showweeknumbers=False, 
        #     cursor="hand2", 
        #     date_pattern= 'y-mm-dd',
        #     borderwidth=0, 
        #     bordercolor='white')
        # start_cal.grid(row=2, column=1)
        start_cal = DateEntry(booking_scrollbar, selectmode='day', width=25, font=body_font)
        start_cal.grid(row=2,column=1, padx=5, pady=5)

        end_cal_label = ctk.CTkLabel(booking_scrollbar, text='Check-Out')
        end_cal_label.grid(row=2,column=2, padx=5, pady=5)
        end_cal = DateEntry(booking_scrollbar, selectmode='day', width=25, font=body_font)
        end_cal.grid(row=2,column=3, padx=5, pady=5)

        floor_label = ctk.CTkLabel(booking_scrollbar, text='Floor')
        floor_label.grid(row=3, column=0, sticky='e', padx=10, pady=5)
        floor_cmbbox = ctk.CTkComboBox(
            booking_scrollbar,
            state='readonly', 
            values=['1st Floor', '2nd Floor', '3rd Floor', '4th Floor - Penthouse'])
        floor_cmbbox.set('1st Floor')
        floor_cmbbox.grid(row=3, column=1, padx=5, pady=5)

        balconey_label = ctk.CTkLabel(booking_scrollbar, text='Balconey')
        balconey_label.grid(row=3, column=2, sticky='e', padx=10, pady=5)
        balconey_cmbbox = ctk.CTkComboBox(
            booking_scrollbar,
            state='readonly', 
            values=['Yes', 'No',])
        balconey_cmbbox.set('No')
        balconey_cmbbox.grid(row=3, column=3, padx=5, pady=5)

        tub_label = ctk.CTkLabel(booking_scrollbar, text='Tub Option')
        tub_label.grid(row=4, column=0, sticky='e', padx=10, pady=5)
        tub_cmbbox = ctk.CTkComboBox(
            booking_scrollbar,
            state='readonly', 
            values=['Spa Tub', 'Jacuzzi Tub', 'No Preference',])
        tub_cmbbox.set('No Preference')
        tub_cmbbox.grid(row=4, column=1, padx=5, pady=5)

        minibar_label = ctk.CTkLabel(booking_scrollbar, text='Minibar')
        minibar_label.grid(row=4, column=2, sticky='e', padx=10, pady=5)
        minibar_cmbbox = ctk.CTkComboBox(
            booking_scrollbar,
            state='readonly', 
            values=['Yes', 'No',])
        minibar_cmbbox.set('No')
        minibar_cmbbox.grid(row=4, column=3, padx=5, pady=5)
        
        room_options_label = ctk.CTkLabel(booking_scrollbar, text="Available Rooms",)
        room_options_label.grid(row=5, column=0, sticky='e', padx=5, pady=5)
        room_options_cmbbox = ctk.CTkComboBox(
            booking_scrollbar,
            state='readonly', 
            values=[''])
        room_options_cmbbox.set('No')
        room_options_cmbbox.grid(row=5, column=1, padx=5, pady=5)

        confirmation_btn = ctk.CTkButton(booking_scrollbar, text='Confirm Booking')
        confirmation_btn.grid(row=6, column=0, columnspan=4, padx=5, pady=10)




    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief='raised', activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief='raised', activebackground="#026AA9")
        menubar.add_cascade(label="Options", menu=filemenu)        
        filemenu.add_command(label="Home Page", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_command(label="Account Profile", command=lambda: parent.show_frame(parent.AccountProfile))        
        filemenu.add_command(label="New Booking", command=lambda: parent.show_frame(parent.NewBooking))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=about)
        help_menu.add_separator()

        return menubar
    
#---------------------------------------- Login PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class LogIn(ctk.CTkFrame):
    def __init__(self, parent, container):
        super().__init__(container)
        self.parent = parent
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1 )
        self.columnconfigure(0, weight=1)


        # Page Elements
        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=0, column=0, padx=0, pady=0)
        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.grid(row=1, column=0, padx=0, pady=0)

        title_font = ctk.CTkFont(family="Times", size=30)
        heading_font = ctk.CTkFont(family="Times", size=20)
        body_font = ctk.CTkFont(family="Times", size=15)

        label = ctk.CTkLabel(top_frame,text='Login Page', font=title_font)  
        label.grid(row=0, column=0, padx=5, pady=10)

        self.user_entry_var = StringVar(self)
        user_entry = ctk.CTkEntry(top_frame,placeholder_text="Username", textvariable=self.user_entry_var) 
        user_entry.grid(row=1, column=0, padx=5, pady=5)

        self.user_pass_var = StringVar(self)
        user_pass= ctk.CTkEntry(top_frame,placeholder_text="Password", textvariable=self.user_pass_var,show="*")  
        user_pass.grid(row=2, column=0, padx=5, pady=5)

        # button = ctk.CTkButton(top_frame,text='Login',command=lambda: parent.show_frame(parent.HomePage))  
        button = ctk.CTkButton(top_frame,text='Login',command=self.login)  
        button.grid(row=3, column=0, padx=5, pady=5)

        checkbox = ctk.CTkCheckBox(top_frame,text='Remember Me')  
        checkbox.grid(row=4, column=0, padx=5, pady=5) 

        signup_label = ctk.CTkLabel(bottom_frame, text="Don't have an account? Sign-up for free!")
        signup_label.grid(row=0, column=0, padx=5, pady=5)
        signup_button = ctk.CTkButton(bottom_frame,text='Create an Account',command='')  
        signup_button.grid(row=1, column=0, padx=5, pady=5)

    def login(self): 
        username = 'admin'
        password = '12345'  
        
        if self.user_entry_var.get() == username and self.user_pass_var.get() == password:  
            messagebox.showinfo(title="Login Successful",message="You have logged in Successfully")  
            self.parent.show_frame(AccountProfile)

        elif self.user_entry_var.get() == username and self.user_pass_var.get() != password:  
            messagebox.showwarning(title='Wrong password',message='Please check your password')  
        
        elif self.user_entry_var.get() != username and self.user_pass_var.get() == password:  
            messagebox.showwarning(title='Wrong username',message='Please check your username')  
        
        else:  
            messagebox.showerror(title="Login Failed",message="Invalid Username and password")

# self.frames = {}
#         self.HomePage = HomePage
#         self.AccountProfile = AccountProfile
#         self.NewBooking = NewBooking
#         self.LogIn = LogIn

#         ## Defining Frames and Packing it
#         for F in {HomePage, NewBooking, AccountProfile, LogIn}:
#             frame = F(self, container)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")    
           
#         self.show_frame(HomePage)

#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         menubar = frame.create_menubar(self)
#         self.configure(menu=menubar)
#         frame.tkraise()


    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief='raised', activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief='raised', activebackground="#026AA9")
        menubar.add_cascade(label="Options", menu=filemenu)        
        filemenu.add_command(label="Home Page", command=lambda: parent.show_frame(parent.HomePage))    
        filemenu.add_command(label="New Booking", command=lambda: parent.show_frame(parent.NewBooking))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=about)
        help_menu.add_separator()

        return menubar
    
#---------------------------------------- Account Profile PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class AccountProfile(ctk.CTkFrame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Account Profile", font=('Times', '20'))
        label.pack(pady=0,padx=0)
        
        message = "Welcome back " + userName
        self.welcome = tk.Label(self,text=message)
        self.welcome.pack(anchor=tk.N)

        ## ADD CODE HERE TO DESIGN THIS PAGE

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief='raised', activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief='raised', activebackground="#026AA9")
        menubar.add_cascade(label="Options", menu=filemenu)        
        filemenu.add_command(label="Home Page", command=lambda: parent.show_frame(parent.HomePage))    
        filemenu.add_command(label="New Booking", command=lambda: parent.show_frame(parent.NewBooking))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=about)
        help_menu.add_separator()

        return menubar

app = BookingApp()
app.mainloop()