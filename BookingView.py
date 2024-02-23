import getpass
import time
import mysql.connector
import customtkinter as ctk
import tkinter as tk
from tkinter import Label, Button, StringVar, Toplevel, messagebox, Menu
from tkcalendar import DateEntry



#-- MODELS -- Database Connection --------------------------------------------------------------------------------------------------------------
connection = mysql.connector.connect(host="localhost",user="root",passwd="microsoftSurface",database="HWBHotels")
cursor = connection.cursor()


#-- CONTROLLERS -- Global variables --------------------------------------------------------------------------------------------------------------
global username_var, password_var, fname_var, lname_var, email_var, phone_var, address_var, birthday_var
userName = '%s!'%(getpass.getuser().capitalize())
main_bgc = "#8AA7A9"
add_new_user = ("INSERT INTO user "
               "(user_name, password, first_name, last_name, address, birth_date, email, phone) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

title_font = ctk.CTkFont(family="Times", size=30)
heading_font = ctk.CTkFont(family="Times", size=20)
body_font = ctk.CTkFont(family="Times", size=15)


#-- CONTROLLERS -- App's functions --------------------------------------------------------------------------------------------------------------
## FUNCTION: About msgbox on menubar
def about():
    messagebox.showinfo('About', "This is a sample Booking Application made by Tahnee Pitter-Duncan. \n\nThis app is made using Python and Tkinter. The Tkinter package is used to build a simple GUI.")

## FUNCTION: Close frame on btn click
def error_destroy():
    err.destroy()

## FUNCTION: Destroy logged in msg
def logg_destroy():
    logg.destroy()
    
    app.show_frame(LoggedIn_HP)

## FUNCTION: Destroy logged in popup
def fail_destroy():
    fail.destroy()

## FRAME: Logged In POPUP
def logged():
    global logg

    logg = Toplevel()
    logg.title("Welcome")
    logg.geometry("200x100")

    Label(logg, text="Welcome {} ".format(username_var.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Enter App", bg="grey", width=8, height=1, command=logg_destroy).pack()

## FUNCTION: Login Fail
def failed():
    global fail

    fail = Toplevel()
    fail.title("Invalid")
    fail.geometry("200x100")

    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()

## FUNCTION: Login Verification
def login_varify():
    user_varify = username_var.get()
    pas_varify = password_var.get()

    sql = "select * from user where user_name = %s and password = %s"
    cursor.execute(sql,[(user_varify),(pas_varify)])
    results = cursor.fetchall()

    if results:
        for i in results:
            logged()
            break
    else:
        failed()

## FUNCTION: Close frame on btn click
def succ_destroy():
    succ.destroy()

    app.show_frame(LoggedIn_HP)

## FUNCTION: Register User
def register_user():
    username_info = username_var.get()
    password_info = password_var.get()
    fname = fname_var.get()
    lname = lname_var.get()
    email = email_var.get()
    phone = phone_var.get()
    addy = address_var.get()
    birthday = birthday_var.get()

    if username_info == "":
        error()
    elif password_info == "":
        error()
    elif fname == "":
        error()
    elif lname == "":
        error()
    elif email == "":
        error()
    elif phone == "":
        error()
    elif addy == "":
        error()
    elif birthday == "":
        error()
    else:
        new_user = (username_info, password_info, fname, lname, addy, birthday, email, phone)
        cursor.execute(add_new_user, new_user)
        connection.commit()

        time.sleep(0.50)

        success()

## FUNCTION FRAME: Successful Registration -> succ_destroy
def success():
    global succ

    succ = Toplevel()
    succ.title("Success")
    succ.geometry("200x100")

    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()

## FUNCTION FRAME: Registration Error -> error_destroy
def error():
    global err

    err = Toplevel()
    err.title("Error")
    err.geometry("200x100")

    Label(err,text="All fields are required..",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()



#-- VIEW -- Main FRAME / CONTAINER --------------------------------------------------------------------------------------------------------------
class BookingApp(ctk.CTk):

    def __init__(self):

        ## Initialize self
        ctk.CTk.__init__(self)
        self.title("HWB Hotels Booking App")
        self.geometry("700x550")
        

        ## Frame configuration
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        ## Initialize views [frames]
        self.frames = {}
        self.HomePage = HomePage
        self.AccountProfile = AccountProfile
        self.NewBooking = NewBooking
        self.LogIn = LogIn
        self.SignUp = SignUp
        self.LoggedIn_HP = LoggedIn_HP


        ## Defining Frames and Packing it
        for F in {HomePage, NewBooking, AccountProfile, LogIn, LoggedIn_HP, SignUp}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")    


        ## Starting view
        self.show_frame(HomePage)


    ## Show views [frames]
    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = frame.create_menubar(self)
        self.configure(menu=menubar)
        frame.tkraise()        ## This line will put the frame on front


#-- VIEW -- Home Page PAGE FRAME / CONTAINER --------------------------------------------------------------------------------------------------------------
class HomePage(ctk.CTkFrame):
    def __init__(self, parent, container):

        ## Load view in main frame
        super().__init__(container)


        ## Configure frame
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1 )

        self.columnconfigure(0, weight=1)

        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=0, column=0, padx=0, pady=0)

        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.grid(row=1, column=0, padx=0, pady=0)

       
        ## Frame Elements
        hp_label = ctk.CTkLabel(top_frame, text="Home Page", font=title_font)
        hp_label.grid(row=0, column=0, pady=10,padx=0)

        welcome_message = 'Welcome to HWB Hotels Booking App!'
        self.welcome_label = ctk.CTkLabel(top_frame,text=welcome_message,font=heading_font)
        self.welcome_label.grid(row=1, column=0, pady=0,padx=0)

        hp_blurb = "Experience the essence of luxury in the heart of Toronto at our boutique hotel.\nSecure your urban sanctuary today and immerse yourself in the vibrant energy\nof the city. Located in the bustling metropolis of Toronto, our boutique gem\npromises an unforgettable stay."
        self.hp_blurb_label = ctk.CTkLabel(top_frame,text=hp_blurb, font=body_font)
        self.hp_blurb_label.grid(row=2, column=0, pady=0,padx=0)

        hp_button_label_msg = "Elevate your travel experience – reserve your spot today!"
        self.hp_button_label = ctk.CTkLabel(bottom_frame,text=hp_button_label_msg,font=heading_font)
        self.hp_button_label.grid(row=0, columnspan=3, sticky='news', pady=15,padx=0)

        signup_btn = ctk.CTkButton(bottom_frame, text="Sign-Up", command=lambda: parent.show_frame(parent.SignUp))
        signup_btn.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        login_btn = ctk.CTkButton(bottom_frame, text="Login", command=lambda: parent.show_frame(parent.LogIn))
        login_btn.grid(row=1, column=1, columnspan=2, padx=20, pady=10)

        
    ## Menubar
    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief="raised", activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief='raised', activebackground="#026AA9")
        menubar.add_cascade(label="Options", menu=filemenu)
        filemenu.add_command(label="Sign-Up", command=lambda: parent.show_frame(parent.SignUp))
        filemenu.add_command(label="Log-In", command=lambda: parent.show_frame(parent.LogIn))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=about)
        help_menu.add_separator()

        return menubar


#-- VIEW -- Login PAGE FRAME / CONTAINER --------------------------------------------------------------------------------------------------------------
class LogIn(ctk.CTkFrame):
    def __init__(self, parent, container):

        ## Load view in main frame
        super().__init__(container)
        self.parent = parent


        ## Configure frame
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1 )

        self.columnconfigure(0, weight=1)

        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=0, column=0, padx=0, pady=0)

        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.grid(row=1, column=0, padx=0, pady=0)


        ## Frame Elements
        label = ctk.CTkLabel(top_frame,text='Login Page', font=title_font)  
        label.grid(row=0, column=0, padx=5, pady=10)

        global username_var 
        username_entry_var = StringVar()
        user_entry = ctk.CTkEntry(top_frame,placeholder_text="Username", textvariable=username_entry_var) 
        user_entry.grid(row=1, column=0, padx=5, pady=5)
        username_var = username_entry_var 

        global password_var
        user_pass_var = StringVar()
        user_pass= ctk.CTkEntry(top_frame,placeholder_text="Password", textvariable=user_pass_var,show="*")  
        user_pass.grid(row=2, column=0, padx=5, pady=5)
        password_var = user_pass_var

        button = ctk.CTkButton(top_frame,text='Login',command=login_varify)  
        button.grid(row=3, column=0, padx=5, pady=5)

        checkbox = ctk.CTkCheckBox(top_frame,text='Remember Me')  
        checkbox.grid(row=4, column=0, padx=5, pady=5) 
        signup_label = ctk.CTkLabel(bottom_frame, text="Don't have an account? Sign-up for free!")
        signup_label.grid(row=0, column=0, padx=5, pady=5)
        signup_button = ctk.CTkButton(bottom_frame,text='Create an Account',command=lambda: parent.show_frame(parent.SignUp))  
        signup_button.grid(row=1, column=0, padx=5, pady=5)


    ## Menubar
    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief="raised", activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief='raised', activebackground="#026AA9")
        menubar.add_cascade(label="Options", menu=filemenu)
        filemenu.add_command(label="Sign-Up", command=lambda: parent.show_frame(parent.SignUp))
        filemenu.add_command(label="Log-In", command=lambda: parent.show_frame(parent.LogIn))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=about)
        help_menu.add_separator()

        return menubar
    

#-- VIEW -- Sign-up PAGE FRAME / CONTAINER --------------------------------------------------------------------------------------------------------------
class SignUp(ctk.CTkFrame):
    def __init__(self, parent, container):

        ## Load view in main frame
        super().__init__(container)
        self.parent = parent

        
        ## Configure frame
        self.rowconfigure(0, weight=1) 
        self.rowconfigure(1, weight=1 )

        self.columnconfigure(0, weight=1)

        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=0, column=0, padx=0, pady=0)

        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.grid(row=1, column=0, padx=0, pady=0)


        ## Frame Elements
        label = ctk.CTkLabel(top_frame,text='Sign-Up Page', font=title_font)  
        label.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

        global username_var
        username_entry_var = StringVar()
        l1 = ctk.CTkLabel(top_frame,text='Username', font=body_font)  
        l1.grid(row=1, column=0)
        user_entry = ctk.CTkEntry(top_frame,placeholder_text="Username", textvariable=username_entry_var) 
        user_entry.grid(row=2, column=0)
        username_var = username_entry_var

        global password_var
        user_pass_var  = StringVar()
        l2 = ctk.CTkLabel(top_frame,text='Password', font=body_font)  
        l2.grid(row=1, column=1)
        user_pass= ctk.CTkEntry(top_frame,placeholder_text="Password", textvariable=user_pass_var,show="*")  
        user_pass.grid(row=2, column=1)
        password_var = user_pass_var
        
        global fname_var
        fname_entry_var = StringVar()
        l3 = ctk.CTkLabel(top_frame,text='First Name', font=body_font)  
        l3.grid(row=3, column=0)
        fname_entry = ctk.CTkEntry(top_frame,placeholder_text="First Name", textvariable=fname_entry_var) 
        fname_entry.grid(row=4, column=0)
        fname_var = fname_entry_var

        global lname_var
        lname_entry_var = StringVar()
        l4 = ctk.CTkLabel(top_frame,text='Last Name', font=body_font)  
        l4.grid(row=3, column=1)
        lname_entry= ctk.CTkEntry(top_frame,placeholder_text="Last Name", textvariable=lname_entry_var)  
        lname_entry.grid(row=4, column=1)
        lname_var = lname_entry_var
        
        global email_var
        email_entry_var = StringVar()
        l5 = ctk.CTkLabel(top_frame,text='Email', font=body_font)  
        l5.grid(row=5, column=0)
        email_entry = ctk.CTkEntry(top_frame,placeholder_text="Email", textvariable=email_entry_var) 
        email_entry.grid(row=6, column=0)
        email_var = email_entry_var

        global phone_var
        phone_entry_var = StringVar()
        l6 = ctk.CTkLabel(top_frame,text='Phone Number', font=body_font)  
        l6.grid(row=5, column=1)
        phone_entry= ctk.CTkEntry(top_frame,placeholder_text="1-XXX-XXX-XXXX", textvariable=phone_entry_var)  
        phone_entry.grid(row=6, column=1)
        phone_var = phone_entry_var

        global address_var
        address_entry_var = StringVar()
        l7 = ctk.CTkLabel(top_frame,text='Address', font=body_font)  
        l7.grid(row=7, column=0)
        address_entry = ctk.CTkEntry(top_frame,placeholder_text="Address", textvariable=address_entry_var) 
        address_entry.grid(row=7, column=1, columnspan=2)
        address_var = address_entry_var

        global birthday_var
        birthday_label = ctk.CTkLabel(top_frame, text='Birthday')
        birthday_label.grid(row=8,column=0, sticky='e')
        birthday_entry_var = StringVar()
        birthday_cal = DateEntry(top_frame, selectmode='day', date_pattern='yyyy/mm/dd', width=25, font=body_font, textvariable=birthday_entry_var)
        birthday_cal.grid(row=8,column=1, columnspan=3)
        birthday_var = birthday_entry_var

        button = ctk.CTkButton(top_frame,text='Sign-Up',command=register_user)  
        button.grid(row=9, column=0, columnspan=4, padx=5, pady=5)

        signup_label = ctk.CTkLabel(bottom_frame, text="Already have an account? Log-in now!")
        signup_label.grid(row=0, column=0, padx=5, pady=5)
        signup_button = ctk.CTkButton(bottom_frame,text='Log-In',command=lambda: parent.show_frame(parent.LogIn))  
        signup_button.grid(row=1, column=0, padx=5, pady=5)

        
    ## Menubar
    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief="raised", activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief='raised', activebackground="#026AA9")
        menubar.add_cascade(label="Options", menu=filemenu)
        filemenu.add_command(label="Sign-Up", command=lambda: parent.show_frame(parent.SignUp))
        filemenu.add_command(label="Log-In", command=lambda: parent.show_frame(parent.LogIn))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=about)
        help_menu.add_separator()

        return menubar


#-- VIEW -- Logged In Home Page PAGE FRAME / CONTAINER --------------------------------------------------------------------------------------------------------------
class LoggedIn_HP(ctk.CTkFrame):
    def __init__(self, parent, container):
        
        ## Load view in main frame
        super().__init__(container)
        
        ## Configure frame
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1 )

        self.columnconfigure(0, weight=1)

        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=0, column=0, padx=0, pady=0)

        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.grid(row=1, column=0, padx=0, pady=0)


        ## Frame Elements
        hp_label = ctk.CTkLabel(top_frame, text="Home Page", font=title_font)
        hp_label.grid(row=0, column=0, pady=10,padx=0)

        welcome_message = "Welcome to HWB Hotels Booking App " + userName + '!'
        self.welcome_label = ctk.CTkLabel(top_frame,text=welcome_message,font=heading_font)
        self.welcome_label.grid(row=1, column=0, pady=0,padx=0)

        hp_blurb = "Experience the essence of luxury in the heart of Toronto at our boutique hotel.\nSecure your urban sanctuary today and immerse yourself in the vibrant energy\nof the city. Located in the bustling metropolis of Toronto, our boutique gem\npromises an unforgettable stay."
        self.hp_blurb_label = ctk.CTkLabel(top_frame,text=hp_blurb, font=body_font)
        self.hp_blurb_label.grid(row=2, column=0, pady=0,padx=0)

        hp_button_label_msg = "Elevate your travel experience – reserve your spot today!"
        self.hp_button_label = ctk.CTkLabel(bottom_frame,text=hp_button_label_msg,font=heading_font)
        self.hp_button_label.grid(row=0, columnspan=3, sticky='news', pady=5,padx=0)

        new_booking_btn = ctk.CTkButton(bottom_frame, text="New Booking", command=lambda: parent.show_frame(parent.NewBooking))
        new_booking_btn.grid(row=1, column=0,  padx=20, pady=10)

        create_btn = ctk.CTkButton(bottom_frame, text="Account Profile", command=lambda: parent.show_frame(parent.AccountProfile))
        create_btn.grid(row=1, column=1,padx=20, pady=10)

        login_btn = ctk.CTkButton(bottom_frame, text="Log Out", command=lambda: parent.show_frame(parent.LogIn))
        login_btn.grid(row=1, column=2,padx=20, pady=10)


    ## Menubar
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


#-- VIEW -- New Booking FRAME / CONTAINER --------------------------------------------------------------------------------------------------------------
class NewBooking(ctk.CTkFrame):
    def __init__(self, parent, container):

        ## Load view in main frame
        super().__init__(container)
        self.parent = parent


        ## Configure frame
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)


        ## Frame Elements
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


    ## Menubar
    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief='raised', activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief='raised', activebackground="#026AA9")
        menubar.add_cascade(label="Options", menu=filemenu)        
        filemenu.add_command(label="Home Page", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_command(label="Account Profile", command=lambda: parent.show_frame(parent.AccountProfile))       
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=about)
        help_menu.add_separator()

        return menubar
    

#-- VIEW -- Account Profile PAGE FRAME / CONTAINER --------------------------------------------------------------------------------------------------------------
class AccountProfile(ctk.CTkFrame):
    def __init__(self, parent, container):

        ## Load view in main frame
        super().__init__(container)
        self.parent = parent


        ## Configure frame
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1 )

        self.columnconfigure(0, weight=1)

        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=0, column=0, padx=0, pady=0)

        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.grid(row=1, column=0, padx=0, pady=0)


        ## Frame Elements
        label = tk.Label(self, text="Account Profile", font=('Times', '20'))
        label.pack(pady=0,padx=0)
        
        message = "Welcome back " + userName
        self.welcome = tk.Label(self,text=message)
        self.welcome.pack(anchor=tk.N)

        
    ## Menubar
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



#-- MAIN -- App creates BookingApp() --------------------------------------------------------------------------------------------------------------
app = BookingApp()
app.mainloop()