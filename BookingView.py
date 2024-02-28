import getpass
import time
import mysql.connector
import customtkinter as ctk
import tkinter as tk
from tkinter import Label, Button, StringVar, Toplevel, messagebox, Menu
from tkcalendar import DateEntry
from datetime import date, datetime



#-- MODELS -- Database Connection --------------------------------------------------------------------------------------------------------------
connection = mysql.connector.connect(host="localhost",user="root",passwd="microsoftSurface",database="hwbhotels")
cursor = connection.cursor()


#-- CONTROLLERS -- Global variables --------------------------------------------------------------------------------------------------------------
global fname_output, username_var, password_var, fname_var, lname_var, email_var, phone_var, address_var, birthday_var, client_no, room_no_var, floor_no_var, balconey_var, tub_var, minibar_var, check_in_var, check_out_var
username_var = ''
fname_var = ''
userName = '%s!'%(getpass.getuser().capitalize())
main_bgc = "#8AA7A9"

add_new_user = ("INSERT INTO user "
               "(user_name, password, first_name, last_name, address, birth_date, email, phone) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
# add_new_booking = ("INSERT INTO booking "
#                "(user_name, client_fname, client_lname, room_no, minibar, check_in, check_out) "
#                "VALUES %(user_name)s, %(client_fname)s, %(client_lname)s, %(room_no)s, %(minibar)s, %(check_in)s, %(check_out)s)")
add_new_booking = ("INSERT INTO booking "
               "(user_name, client_fname, client_lname, room_no, minibar, check_in, check_out) "
               "VALUES %s, %s, %s, %s, %s, %s, %s)")


#-- CONTROLLERS -- App's functions --------------------------------------------------------------------------------------------------------------

## CLASS: Logged in user
class LoggedInUser():
        username = ''
        fname = ''

        def return_username(fname):
            text = "Welcome back {}!".format(fname)
            return text , fname
        
        # def __str__(fname):
        #     return f'Welcome back {fname}!'
        
        def welcome(fname):
            # global username_var, password_var
            user_varify = username_var
            pas_varify = password_var

            sql = "select first_name from user where user_name = %s and password = %s"

            cursor.execute(sql,[(user_varify),(pas_varify)])
            results = cursor.fetchall()

            if results:
                for i in results:
                    fname_list = list(map(list, results))
                    fname_info = fname_list[0]

                    fname = fname_info[0]

                    setattr(LoggedInUser, 'fname', fname)

                    print(f"Welcome back {fname}!")
                return f"Welcome back {fname}!"
            else:
                print("Welcome!")
                return "Welcome back user!"


# def test_btn_func():
#             print('chicken')
#             print(LoggedInUser.username)
#             print(fname_var)

def welcome_msg(fname):
    global text
    text = "Welcome back {}!".format(fname)

    print(text)

    # return "Welcome back {}!".format(fname)
    return text

def welcomeuserhp():
    global fname_var
    user_varify = username_var.get()
    pas_varify = password_var.get()

    sql = "select first_name from user where user_name = %s and password = %s"

    cursor.execute(sql,[(user_varify),(pas_varify)])
    results = cursor.fetchall()

    if results:
        for i in results:

            user_info_list = list(map(list, results)) ## Convert list of tuples into a list
            user_info = user_info_list[0] ## Assign list to variable

            fname_var = user_info[0]
            msg = "Welcome back {}!".format(fname_var)

            print(fname_var)
            print(msg)
            return "Welcome back {}!".format(fname_var)

def return_username(username,fname):
    global username_var
    username_var = LoggedInUser.username

    global fname_var
    fname_var = LoggedInUser.fname

    if username_var != '':
        print('Name is: {}'.format(fname_var))
        print('Username is: {}'.format(username_var))
    # elif username_var == '':   
    #     print('No user logged in yet.')

    else:
        print('No user logged in yet...')
        print("-------------------------------------")
        
    return username_var, fname_var

def letstryagain_fname(fname):
    global fname_var
    fname_var = fname
    user_in = LoggedInUser() 
    user_in.fname = fname_var
    print(user_in)

    return user_in

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

    Label(logg, text="Welcome {} ".format(username_var), fg="green", font="bold").pack()
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
    global username_var, password_var,fname_var, lname_var, address_var, birthday_var, email_var, phone_var

    user_varify = username_var.get()
    pas_varify = password_var.get()

    sql = "select * from user where user_name = %s and password = %s"

    cursor.execute(sql,[(user_varify),(pas_varify)])
    results = cursor.fetchall()

    if results:
        for i in results:
            username_var = user_varify

            sql = "select first_name, last_name, address, birth_date, email, phone from user where user_name = %s and password = %s"
            cursor.execute(sql,[(user_varify),(pas_varify)])
            results = cursor.fetchall()

            user_info_list = list(map(list, results)) ## Convert list of tuples into a list
            user_info = user_info_list[0] ## Assign list to variable

            fname_var = user_info[0]
            lname_var = user_info[1]
            address_var = user_info[2]
            birthday_var = user_info[3]
            email_var = user_info[4]
            phone_var = user_info[5]
            setattr(LoggedInUser, 'username', username_var)
            setattr(LoggedInUser, 'fname', fname_var)
            setattr(LoggedInUser, 'lname', lname_var)

            print("-------------------------------------\n")
            print("Logged In User's Information:\n")
            
            print('Username: {}'.format(username_var))
            print('First Name: {}'.format(fname_var))
            print('Last Name: {}'.format(lname_var))
            print('Address: {}'.format(address_var))
            print('Birthday: {}'.format(birthday_var))
            print('Email: {}'.format(email_var))
            print('Phone Number: {}\n'.format(phone_var))
            # print('Class LoggedInUser username attribute: '.format(LoggedInUser.username)) ## Does not work
            
            print(LoggedInUser.username)
            return_username(LoggedInUser.username, LoggedInUser.fname)
            print('\n')

            # welcome_msg(LoggedInUser.fname)
            print(f"Welcome back {fname_var}")
            # letstryagain_fname(username_var)
            print("*------------------------------------*\n")

            # global fname_output
            # fname_output = LoggedInUser.fname

            logged()
            fname_var = welcome_msg
        return username_var, fname_var, lname_var, address_var, birthday_var, email_var, phone_var, LoggedInUser.fname
            
    else:
        failed()

# def btnclicked():
#     # print("New booking entered into database")
#     # global fname_var, lname_var, phone_var, email_var, check_in_var, check_out_var, floor_no_var, balconey_var, tub_var, minibar_var

#     check_in = check_in_var.get()
#     check_out = check_out_var.get()

#     formatstring = "- AVAILABLE: Floor #: {0} | Room #: {1} | Split Room: {2} |\nBed Amount: {3} | Balconey: {4} | Tub Style: {5} | Minibar: {6}\n"
#     sql = """
#         SELECT 
#         r.floor_no, r.room_no, r.split_room, r.bed_no, r.balconey, r.tub_style, r.minibar, 
#         b.check_in, b.check_out 
#         FROM hwbhotels.room r 
#         LEFT JOIN hwbhotels.booking b 
#         ON r.room_no = b.room_no 
#         AND b.check_in NOT BETWEEN CAST(%s AS DATE) and CAST(%s AS DATE) 
#         AND b.check_out NOT BETWEEN CAST(%s AS DATE) and CAST(%s AS DATE)"""
    
#     cursor.execute(sql, [(check_in), (check_out), (check_in), (check_out)])
#     availability = cursor.fetchall()

#     available_options = []
#     for available in availability:
#         # print("- {}".format(available))
#         option = formatstring.format(*available)
#         available_options.append(option)
#         print(option)
#     print(f'Available Options\n {available_options}')
            

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

## FUNCTION FRAME: Successful Booking -> succ_destroy
def successful_booking_entry():
    global succ

    succ = Toplevel()
    succ.title("Success")
    succ.geometry("200x100")

    Label(succ, text="Booking successful...", fg="green", font="bold").pack()
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

## FUNCTION: New booking entry
def new_booking():
    username = username_var
    fname = fname_var
    lname = lname_var
    room_no = room_no_var
    minibar = minibar_var
    uin = check_in_var.get_date()
    uout = check_out_var.get_date()

    checkin = uin.strftime("%Y-%m-%d")
    checkout = uout.strftime("%Y-%m-%d")

    if username == "":
        error()
    elif fname == "":
        error()
    elif lname == "":
        error()
    elif room_no == "":
        error()
    elif minibar == "":
        error()
    elif checkin == "":
        error()
    elif checkout == "":
        error()
    else:
        username = username_var.get()
        fname = fname_var.get()
        lname = lname_var.get()
        room_no = room_no_var.get()
        minibar = minibar_var.get()
        booking = (username_var, fname, lname, room_no, minibar, checkin, checkout)
        cursor.execute(add_new_booking, booking)
        connection.commit()

        time.sleep(0.50)

        successful_booking_entry()
    
## FUNCTION: Booking history
## FUNCTION: Print booking history


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

        title_font = ctk.CTkFont(family="Times", size=30)
        heading_font = ctk.CTkFont(family="Times", size=20)
        body_font = ctk.CTkFont(family="Times", size=15)

       
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

        title_font = ctk.CTkFont(family="Times", size=30)
        heading_font = ctk.CTkFont(family="Times", size=20)
        body_font = ctk.CTkFont(family="Times", size=15)


        ## Frame Elements
        label = ctk.CTkLabel(top_frame,text='Login Page', font=title_font)  
        label.grid(row=0, column=0, padx=5, pady=10)

        global username_var 
        user_entry = ctk.CTkEntry(top_frame,placeholder_text="Username") 
        user_entry.grid(row=1, column=0, padx=5, pady=5)
        username_var = user_entry

        global password_var
        user_pass= ctk.CTkEntry(top_frame,placeholder_text="Password",show="*")  
        user_pass.grid(row=2, column=0, padx=5, pady=5)
        password_var = user_pass

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
        # filemenu.add_command(label="Log-In", command=lambda: parent.show_frame(parent.LogIn))
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

        title_font = ctk.CTkFont(family="Times", size=30)
        heading_font = ctk.CTkFont(family="Times", size=20)
        body_font = ctk.CTkFont(family="Times", size=15)


        ## Frame Elements
        label = ctk.CTkLabel(top_frame,text='Sign-Up Page', font=title_font)  
        label.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

        global username_var
        l1 = ctk.CTkLabel(top_frame,text='Username', font=body_font)  
        l1.grid(row=1, column=0)
        user_entry = ctk.CTkEntry(top_frame,placeholder_text="Username") 
        user_entry.grid(row=2, column=0)
        username_var = user_entry

        global password_var
        l2 = ctk.CTkLabel(top_frame,text='Password', font=body_font)  
        l2.grid(row=1, column=1)
        user_pass= ctk.CTkEntry(top_frame,placeholder_text="Password",show="*")  
        user_pass.grid(row=2, column=1)
        password_var = user_pass
        
        global fname_var
        l3 = ctk.CTkLabel(top_frame,text='First Name', font=body_font)  
        l3.grid(row=3, column=0)
        fname_entry = ctk.CTkEntry(top_frame,placeholder_text="First Name") 
        fname_entry.grid(row=4, column=0)
        fname_var = fname_entry

        global lname_var
        l4 = ctk.CTkLabel(top_frame,text='Last Name', font=body_font)  
        l4.grid(row=3, column=1)
        lname_entry= ctk.CTkEntry(top_frame,placeholder_text="Last Name")  
        lname_entry.grid(row=4, column=1)
        lname_var = lname_entry
        
        global email_var
        l5 = ctk.CTkLabel(top_frame,text='Email', font=body_font)  
        l5.grid(row=5, column=0)
        email_entry = ctk.CTkEntry(top_frame,placeholder_text="Email") 
        email_entry.grid(row=6, column=0)
        email_var = email_entry

        global phone_var
        l6 = ctk.CTkLabel(top_frame,text='Phone Number', font=body_font)  
        l6.grid(row=5, column=1)
        phone_entry= ctk.CTkEntry(top_frame,placeholder_text="1-XXX-XXX-XXXX")  
        phone_entry.grid(row=6, column=1)
        phone_var = phone_entry

        global address_var
        l7 = ctk.CTkLabel(top_frame,text='Address', font=body_font)  
        l7.grid(row=7, column=0)
        address_entry = ctk.CTkEntry(top_frame,placeholder_text="Address") 
        address_entry.grid(row=7, column=1, columnspan=2)
        address_var = address_entry

        global birthday_var
        birthday_label = ctk.CTkLabel(top_frame, text='Birthday')
        birthday_label.grid(row=8,column=0, sticky='e')
        birthday_cal = DateEntry(top_frame, selectmode='day', date_pattern='yyyy/mm/dd', width=25, font=body_font)
        birthday_cal.grid(row=8,column=1, columnspan=3)
        birthday_var = birthday_cal

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

        title_font = ctk.CTkFont(family="Times", size=30)
        heading_font = ctk.CTkFont(family="Times", size=20)
        body_font = ctk.CTkFont(family="Times", size=15)


        ## Frame Elements
        hp_label = ctk.CTkLabel(top_frame, text="Welcome Back!", font=title_font)
        hp_label.grid(row=0, column=0, pady=10,padx=0)

        hp_blurb = "Secure your stay in the bustling metropolis of Toronto at our boutique today."
        self.hp_blurb_label = ctk.CTkLabel(top_frame,text=hp_blurb, font=body_font)
        self.hp_blurb_label.grid(row=1, column=0, pady=0,padx=0)

        hp_button_label_msg = f"We're here to elevate your travel experience – reserve your spot today!"
        self.hp_button_label = ctk.CTkLabel(bottom_frame,text=hp_button_label_msg,font=heading_font)
        self.hp_button_label.grid(row=0, columnspan=3, sticky='news', pady=5,padx=0)

        new_booking_btn = ctk.CTkButton(bottom_frame, text="New Booking", command=lambda: parent.show_frame(parent.NewBooking))
        new_booking_btn.grid(row=1, column=0,  padx=20, pady=10)

        create_btn = ctk.CTkButton(bottom_frame, text="Account Profile", command=lambda: parent.show_frame(parent.AccountProfile))
        create_btn.grid(row=1, column=1,padx=20, pady=10)

        login_btn = ctk.CTkButton(bottom_frame, text="Log Out", command=lambda: parent.show_frame(parent.LogIn))
        login_btn.grid(row=1, column=2,padx=20, pady=10)

        # test_btn = ctk.CTkButton(bottom_frame, text="Test Button", command=test_btn_func)
        # test_btn.grid(row=2, column=0, columnspan=3 ,padx=20, pady=10)

        


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

        title_font = ctk.CTkFont(family="Times", size=30)
        heading_font = ctk.CTkFont(family="Times", size=20)
        body_font = ctk.CTkFont(family="Times", size=15)
        list_font = ctk.CTkFont(family="Times", size=10)

        label = ctk.CTkLabel(top_frame, text="New Booking", font=title_font)
        label.grid(row=0, column=0, columnspan=3, sticky='nw', pady=0,padx=0)

        booking_msg = "Fill out the form below to book your stay with us!"
        self.booking_label = ctk.CTkLabel(top_frame,text=booking_msg, font=body_font)
        self.booking_label.grid(row=1, columnspan=3, sticky='nw', pady=0,padx=0)

        booking_scrollbar = ctk.CTkScrollableFrame(
            scroll_frame,
            width=570,
            height=200,
            label_text="Booking Form",

            label_font=heading_font,
            label_anchor = "center", # "w",  # n, ne, e, se, s, sw, w, nw, center
            border_width=3,
            border_color="black",

            scrollbar_fg_color="light gray",
            scrollbar_button_color="gray",
            scrollbar_button_hover_color = "black",
            corner_radius = 10,)
        booking_scrollbar.grid(row = 0, column = 0, columnspan=2)
        
        global fname_var
        fname_label = ctk.CTkLabel(booking_scrollbar, text='First Name')
        fname_label.grid(row=0, column=0, sticky='e', padx=10, pady=5)
        fname_entry = ctk.CTkEntry(booking_scrollbar, placeholder_text='First Name')
        fname_entry.grid(row=0, column=1, padx=5, pady=5)
        fname_var = fname_entry
        # fname_entry.configure(state='readonly')

        global lname_var
        lname_label = ctk.CTkLabel(booking_scrollbar, text='Last Name')
        lname_label.grid(row=0, column=2, sticky='e', padx=10, pady=5)
        lname_entry = ctk.CTkEntry(booking_scrollbar, placeholder_text='Last Name')
        lname_entry.grid(row=0, column=3, padx=5, pady=5)
        lname_var = lname_entry

        global phone_var
        phone_num_label = ctk.CTkLabel(booking_scrollbar, text='Phone Number')
        phone_num_label.grid(row=1, column=0, sticky='e', padx=10, pady=5)
        phone_num_entry = ctk.CTkEntry(booking_scrollbar, placeholder_text='1-XXX-XXX-XXXX')
        phone_num_entry.grid(row=1, column=1, padx=5, pady=5)
        phone_var = phone_num_entry

        global email_var
        email_label = ctk.CTkLabel(booking_scrollbar, text='Email')
        email_label.grid(row=1, column=2, sticky='e', padx=10, pady=5)
        email_entry = ctk.CTkEntry(booking_scrollbar, placeholder_text="Email Address")
        email_entry.grid(row=1, column=3, padx=5, pady=5)
        email_var = email_entry

        global check_in_var
        start_cal_label = ctk.CTkLabel(booking_scrollbar, text='Check-In')
        start_cal_label.grid(row=2, column=0, sticky='e', padx=10, pady=5)
        start_cal = DateEntry(booking_scrollbar, selectmode='day', date_pattern='yyyy/mm/dd', width=25, font=body_font)
        start_cal.grid(row=2,column=1, padx=5, pady=5)
        check_in_var = start_cal

        global check_out_var
        end_cal_label = ctk.CTkLabel(booking_scrollbar, text='Check-Out')
        end_cal_label.grid(row=2,column=2, padx=5, pady=5)
        end_cal = DateEntry(booking_scrollbar, selectmode='day', date_pattern='yyyy/mm/dd', width=25, font=body_font)
        end_cal.grid(row=2,column=3, padx=5, pady=5)
        check_out_var = end_cal

        # global floor_no_var
        # floor_label = ctk.CTkLabel(booking_scrollbar, text='Floor')
        # floor_label.grid(row=3, column=0, sticky='e', padx=10, pady=5)
        # floor_cmbbox = ctk.CTkComboBox(
        #     booking_scrollbar,
        #     state='readonly', 
        #     values=['1st Floor', '2nd Floor', '3rd Floor', '4th Floor - Penthouse'])
        # floor_cmbbox.set('1st Floor')
        # floor_cmbbox.grid(row=3, column=1, padx=5, pady=5)
        # floor_no_var = floor_cmbbox

        # global balconey_var
        # balconey_label = ctk.CTkLabel(booking_scrollbar, text='Balconey')
        # balconey_label.grid(row=3, column=2, sticky='e', padx=10, pady=5)
        # balconey_cmbbox = ctk.CTkComboBox(
        #     booking_scrollbar,
        #     state='readonly', 
        #     values=['Yes', 'No',])
        # balconey_cmbbox.set('No')
        # balconey_cmbbox.grid(row=3, column=3, padx=5, pady=5)
        # balconey_var = balconey_cmbbox

        # global tub_var
        # tub_label = ctk.CTkLabel(booking_scrollbar, text='Tub Option')
        # tub_label.grid(row=4, column=0, sticky='e', padx=10, pady=5)
        # tub_cmbbox = ctk.CTkComboBox(
        #     booking_scrollbar,
        #     state='readonly', 
        #     values=['Spa Tub', 'Jacuzzi Tub', 'No Preference',])
        # tub_cmbbox.set('No Preference')
        # tub_cmbbox.grid(row=4, column=1, padx=5, pady=5)
        # tub_var = tub_cmbbox

        # global minibar_var
        # minibar_label = ctk.CTkLabel(booking_scrollbar, text='Minibar')
        # minibar_label.grid(row=4, column=2, sticky='e', padx=10, pady=5)
        # minibar_cmbbox = ctk.CTkComboBox(
        #     booking_scrollbar,
        #     state='readonly', 
        #     values=['Yes', 'No',])
        # minibar_cmbbox.set('No')
        # minibar_cmbbox.grid(row=4, column=3, padx=5, pady=5)
        # minibar_var = minibar_cmbbox

        def room_cmbx_update(room_options):
            room_cmbx.configure(values=room_options)
            # room_cmbx.configure(values=[room_options])
            # room_cmbx.set(values)

        def add_label(list_item):
            global label
            label=ctk.CTkLabel(availability_box, text=list_item, font=list_font)
            label.grid()
        
        def available_rooms():

            uin = check_in_var.get_date()
            uout = check_out_var.get_date()

            checkin = uin.strftime("%Y-%m-%d")
            checkout = uout.strftime("%Y-%m-%d")

            formatstring = "- AVAILABLE: Floor #: {0} | Room #: {1} | Split Room: {2} | Bed Amount: {3} | Balconey: {4} | Tub Style: {5} | Minibar: {6}"
            sql = """
                SELECT 
                r.floor_no, r.room_no, r.split_room, r.bed_no, r.balconey, r.tub_style, r.minibar,
                b.check_in, b.check_out 
                FROM hwbhotels.room r
                LEFT JOIN hwbhotels.booking b
                ON r.room_no = b.room_no
                WHERE b.check_in NOT BETWEEN CONVERT(%s , DATE) and CONVERT(%s , DATE)
                AND b.check_out NOT BETWEEN CONVERT(%s , DATE) and CONVERT(%s , DATE)
                OR b.check_in IS NULL AND b.check_out IS NULL    
                """

            cursor.execute(sql, [checkin, checkout, checkin, checkout])
            availability = cursor.fetchall()

            listing_msg = f"Listing the available units between {checkin} ~ {checkout}..."
            print(listing_msg)
            availability_results_label.configure(text=listing_msg)

            available_options = []
            for available in availability:
                option = formatstring.format(*available)
                available_options.append(option)
                add_label(option)
                print(option)
            
            formatstring2 = "Room #: {0} | Bed Amount: {1}"
            sql = """
                SELECT r.room_no, r.bed_no 
                FROM hwbhotels.room r
                LEFT JOIN hwbhotels.booking b
                ON r.room_no = b.room_no
                WHERE b.check_in NOT BETWEEN CONVERT(%s , DATE) and CONVERT(%s , DATE)
                AND b.check_out NOT BETWEEN CONVERT(%s , DATE) and CONVERT(%s , DATE)
                OR b.check_in IS NULL AND b.check_out IS NULL    
                """
            room_options = []
            cursor.execute(sql, [checkin, checkout, checkin, checkout])
            room_list = cursor.fetchall()
            for room in room_list:
                room = formatstring2.format(*room)
                room_options.append(room)
                # room_cmbx_update(room)
                # add_label(option)
                # print(option)
            room_cmbx_update(room_options)
            print("\n*------------------------------------*\n")
            
        
        check_availability_btn = ctk.CTkButton(booking_scrollbar, text='Check room availability', command=available_rooms)
        check_availability_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

        availability_box = ctk.CTkScrollableFrame(
            booking_scrollbar,
            width=380,
            height=30,
            fg_color="white",

            label_text='Available Rooms',
            label_font=body_font,
            label_anchor="center",

            border_width=2,
            border_color="black",

            scrollbar_fg_color="light gray",
            scrollbar_button_color="gray",
            scrollbar_button_hover_color = "black",
            corner_radius = 10)
        availability_box.grid(row=6, rowspan=1,column=0, columnspan=4, padx=5, pady=10)
        availability_box._scrollbar.configure(height=60)

        availability_results_label = ctk.CTkLabel(availability_box, text='', font=body_font)
        availability_results_label.grid(row=0, column=0, columnspan=3)

        # rooms_list_label = ctk.CTkLabel(availability_box, text='', font=list_font)
        # rooms_list_label.grid(row=1, column=0, columnspan=3)

        global room_no_var
        room_label = ctk.CTkLabel(booking_scrollbar, text='Select Room')
        room_label.grid(row=7, column=0, sticky='e', padx=10, pady=5)
        room_cmbx = ctk.CTkComboBox(
            booking_scrollbar,
            state='readonly', 
            values=['',])
        room_cmbx.set('None selected')
        room_cmbx.grid(row=7, column=1, padx=5, pady=5)
        room_no_var = room_cmbx

        global minibar_var
        minibar_label = ctk.CTkLabel(booking_scrollbar, text='Minibar Option')
        minibar_label.grid(row=7, column=2, sticky='e', padx=10, pady=5)
        minibar_cmbbox = ctk.CTkComboBox(
            booking_scrollbar,
            state='readonly', 
            values=['Yes', 'No',])
        minibar_cmbbox.set('No')
        minibar_cmbbox.grid(row=7, column=3, padx=5, pady=5)
        minibar_var = minibar_cmbbox

        confirmation_btn = ctk.CTkButton(booking_scrollbar, text='Confirm Booking', command=new_booking)
        confirmation_btn.grid(row=8, column=0, columnspan=4, padx=5, pady=10)


    ## Menubar
    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief='raised', activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief='raised', activebackground="#026AA9")
        menubar.add_cascade(label="Options", menu=filemenu)        
        filemenu.add_command(label="Home Page", command=lambda: parent.show_frame(parent.LoggedIn_HP))
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

        title_font = ctk.CTkFont(family="Times", size=30)
        heading_font = ctk.CTkFont(family="Times", size=20)
        body_font = ctk.CTkFont(family="Times", size=15)


        ## Frame Elements
        label = tk.Label(self, text="Account Profile", font=('Times', '20'))
        label.grid(pady=0,padx=0)
        
        message = "Welcome back " + userName
        self.welcome = tk.Label(self,text=message)
        self.welcome.grid()

        
    ## Menubar
    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief='raised', activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief='raised', activebackground="#026AA9")
        menubar.add_cascade(label="Options", menu=filemenu)        
        filemenu.add_command(label="Home Page", command=lambda: parent.show_frame(parent.LoggedIn_HP))    
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
return_username(username_var, fname_var)
LoggedInUser()
app = BookingApp()
app.mainloop()
fname_var = LoggedInUser.fname