from __future__ import print_function
from datetime import date, datetime
import pymysql 
import mysql.connector
from mysql.connector import errorcode
	

 
# ---- Create a connection object ------------------------------------------------------------------------------------------------------------------
Host = "localhost"                     # IP address of the MySQL database server 
User = "root"                          # User name of the database server 
Password = "microsoftSurface"          # Password for the database user 
connection = pymysql.connect(host=Host, user=User, password=Password) 

# Create a cursor object 
cursor = connection.cursor() 



# ---- Create HWB Hotels Schema --------------------------------------------------------------------------------------------------------------------
DB_NAME = 'HWBHotels'

## Tables 
TABLES = {}
TABLES['user'] = (
    "CREATE TABLE `user` ("
    "  `client_no` int NOT NULL AUTO_INCREMENT,"
    "  `emp_status` enum('N','Y') NOT NULL,"
    "  `user_name` varchar(11) NOT NULL,"
    "  `password` varchar(20) NOT NULL,"
    "  `first_name` varchar(20) NOT NULL,"
    "  `last_name` varchar(50) NOT NULL,"
    "  `address` varchar(50),"
    "  `birth_date` date NOT NULL,"
    "  `email` varchar(50) NOT NULL,"
    "  `phone` varchar(14) NOT NULL,"
    "  `creation_date` timestamp DEFAULT CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`client_no`), UNIQUE KEY `email` (`email`), UNIQUE KEY `user_name` (`user_name`)"
    ") ENGINE=InnoDB")

TABLES['room'] = (
    "CREATE TABLE `room` ("
    "  `room_id` int NOT NULL AUTO_INCREMENT,"
    "  `location` varchar(15) NOT NULL,"
    "  `floor_no` int(1) NOT NULL,"
    "  `room_no` int(3) NOT NULL,"
    "  `split_room` enum('N','Y') NOT NULL,"
    "  `bed_no` int(1) NOT NULL,"
    "  `balconey` enum('N','Y') NOT NULL,"
    "  `tub_style` varchar(20) NOT NULL,"
    "  `minibar` enum('N','Y') DEFAULT 'Y',"
    "  PRIMARY KEY (`room_id`), UNIQUE KEY `room_no` (`room_no`)"
    ") ENGINE=InnoDB")

TABLES['booking'] = (
    "CREATE TABLE `booking` ("
    "  `booking_no` int NOT NULL AUTO_INCREMENT,"
    "  `client_no` int NOT NULL,"
    "  `user_name` varchar(11),"
    "  `client_fname` varchar(20) NOT NULL,"
    "  `client_lname` varchar(50) NOT NULL,"
    "  `email` varchar(50),"
    "  `phone` varchar(11),"
    "  `room_no` int(3) NOT NULL,"
    "  `check_in` date NOT NULL,"
    "  `check_out` date NOT NULL,"
    "  `minibar` enum('N','Y') DEFAULT 'N',"
    "  PRIMARY KEY (`booking_no`), KEY `check_in` (`check_in`), KEY `check_out` (`check_out`),"
    "  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`client_no`) REFERENCES `user` (`client_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`user_name`) REFERENCES `user` (`user_name`) ON DELETE CASCADE,"
    "  CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`email`) REFERENCES `user` (`email`) ON DELETE CASCADE,"
    "  CONSTRAINT `booking_ibfk_4` FOREIGN KEY (`room_no`) REFERENCES `room` (`room_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")


## Create database
cursor.execute("DROP DATABASE {}".format(DB_NAME))
print("*------------------------------------*")
print('Existing database dropped!')
print("*------------------------------------*")

try:
    with connection.cursor() as cur:
        cur.execute("CREATE DATABASE HWBHotels")
        print('Created database: {}'.format(DB_NAME))
except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
connection.commit()
print("*------------------------------------*")

## Create tables
print("Creating tables...\n")
connection = pymysql.connect(host=Host, user=User, password=Password, db=DB_NAME) 
cursor = connection.cursor() 

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("  - Creating table [{}]: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
            print(err.msg)
    else:
        print("OK")
connection.commit()
print("\n-------------------------------------")



## ---- Creating table entries -----------------------------------------------------------------------------------------------------------------
today = datetime.now().date()
add_full_user = ("INSERT INTO user "
               "(user_name, password, first_name, last_name, address, birth_date, email, phone, creation_date) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %(today)s)")
add_user = ("INSERT INTO user "
               "(user_name, password, first_name, last_name, birth_date, email, phone, creation_date) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
admin = ('Admin', '1234abcd1234', 'Tahnee', 'Duncan', date(1997, 5, 13), 'admin@admin.com', 14169670001, today)
admin_user = ('Admin_User', '1234abcd1234', 'Tina', 'Snow', date(1995, 2, 15), 'tina_snow@admin.com', 14169670000, today)
test_user_1 = ('TestUserOne', '1234abcd1235', 'TestOne', 'UserOne', date(1985, 5, 8), 'test_user1@abc.com', 14169671111, today)
test_user_2 = ('TestUserTwo', '1234abcd1236', 'TestTwo', 'UserTwo', date(2001, 11, 28), 'test_user2@abc.com', 14169672222, today)
cursor.execute(add_user, admin )
connection.commit()
cursor.execute(add_user, admin_user)
connection.commit()
cursor.execute(add_user, test_user_1)
connection.commit()
cursor.execute(add_user, test_user_2)
connection.commit()


add_room = ("INSERT INTO room "
               "(location, floor_no, room_no, split_room, bed_no, balconey, tub_style, minibar) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
room101 = ('Toronto', 1, 101, 'N', 1, 'N', 'Rain Shower', 'Y')
room102 = ('Toronto', 1, 102, 'N', 2, 'N', 'Rain Shower', 'Y')
room103 = ('Toronto', 1, 103, 'Y', 4, 'Y', 'Jacuzzi Tub', 'Y')
room201 = ('Toronto', 2, 201, 'Y', 2, 'N', 'Spa Bathtub', 'Y')
room202 = ('Toronto', 2, 202, 'Y', 3, 'N', 'Rain Shower', 'Y')
room203 = ('Toronto', 2, 203, 'N', 1, 'Y', 'Jacuzzi Tub', 'Y')
room301 = ('Toronto', 3, 301, 'Y', 2, 'N', 'Jacuzzi Tub', 'Y')
room302 = ('Toronto', 3, 302, 'N', 2, 'N', 'Spa Bathtub', 'Y')
room303 = ('Toronto', 3, 303, 'Y', 4, 'Y', 'Jacuzzi Tub', 'Y')
penthouse = ('Toronto', 4, 401, 'Y', 6, 'Y', 'Jacuzzi Tub', 'Y')
cursor.execute(add_room, room101)
connection.commit()
cursor.execute(add_room, room102)
connection.commit()
cursor.execute(add_room, room103)
connection.commit()
cursor.execute(add_room, room201)
connection.commit()
cursor.execute(add_room, room202)
connection.commit()
cursor.execute(add_room, room203)
connection.commit()
cursor.execute(add_room, room301)
connection.commit()
cursor.execute(add_room, room302)
connection.commit()
cursor.execute(add_room, room303)
connection.commit()
cursor.execute(add_room, penthouse)
connection.commit()


add_booking = ("INSERT INTO booking "
               "(client_no, user_name, client_fname, client_lname, room_no, check_in, check_out) "
               "VALUES (%(client_no)s, %(user_name)s, %(client_fname)s, %(client_lname)s, %(room_no)s, %(check_in)s, %(check_out)s)")

booking1 = {
    'client_no': 1,
    'user_name': 'Admin_User',
    'client_fname':'Tina', 
    'client_lname':'Snow', 
    'room_no':101, 
    'check_in':'2024-03-15', 
    'check_out':'2024-03-18'}
booking2 = {
    'client_no': 2,
    'user_name': 'TestUserOne',
    'client_fname':'TestOne', 
    'client_lname':'UserOne', 
    'room_no':303, 
    'check_in':'2024-03-15', 
    'check_out':'2024-03-25'}
booking3 = {
    'client_no': 3,
    'user_name': 'TestUserTwo',
    'client_fname':'TestTwo', 
    'client_lname':'UserTwo', 
    'room_no':401, 
    'check_in':'2024-03-22', 
    'check_out':'2024-03-25'}
cursor.execute(add_booking, booking1)
cursor.execute(add_booking, booking2)
cursor.execute(add_booking, booking3)
connection.commit()



# ---- Show entries in server -----------------------------------------------------------------------------------------------------------------
## Show all databases
cursor.execute("SHOW DATABASES")       # SQL command      
databaseList = cursor.fetchall()       # Fetch all objects [databases] in cursor
print("Listing all databases in server ...")
for database in databaseList:          # For every database in database list variable   
    print("- {}".format(database))                    # Print to Console each one
connection.commit()
print("\n-------------------------------------")
   
## Show all tables in HWB Hotels DB
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'HWBHotels'")
tableList = cursor.fetchall()
print("Listing all the tables in {} database ...".format(DB_NAME))
for table in tableList:
    print("- {}".format(table))                    # Print to Console each one
connection.commit()
print("\n-------------------------------------")
    
## Show entries in user table
print('Users - Name List:')
cursor.execute("SELECT client_no, first_name, last_name FROM HWBHotels.user")
clientno = cursor.fetchall()
for client in clientno:
    print("- {}".format(client))
connection.commit()
print("\n-------------------------------------")

## Show entries in room table
print("Listing all rooms in HWB Hotels [Toronto Location] ...")
cursor.execute("SELECT floor_no, room_no, bed_no FROM HWBHotels.room")
roomList = cursor.fetchall()
for room in roomList:
    print("- {}".format(room))
connection.commit()
print("\n-------------------------------------")

## Show entries in booking table
print("Listing all bookings for HWB Hotels [Toronto Location] ...")
cursor.execute("SELECT booking_no, client_no, room_no, check_in, check_out FROM HWBHotels.booking")
bookingList = cursor.fetchall()
for booking in bookingList:
    print("- {}".format(booking))
connection.commit()
print("\n-------------------------------------")

## Closing message
print("HWB Hotels database has officially been set-up & populated with \nsample data!\nConnection to server will now close. Goodbye.\n")
print("-------------------------------------\n")



## ---- Close connection -----------------------------------------------------------------------------------------------------------------
cursor.close()
connection.close()                     
