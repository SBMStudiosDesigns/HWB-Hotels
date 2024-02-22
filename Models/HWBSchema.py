from __future__ import print_function
from datetime import date, datetime
from pandas import to_datetime
import pandas
import pymysql 
import mysql.connector
from mysql.connector import errorcode
	

# Schema Variables ----------------------------------------------------------------------------------------------------------------------------
## Database name
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
    "  `birth_date` date NOT NULL,"
    "  `email` varchar(50) NOT NULL,"
    "  `phone` varchar(11) NOT NULL,"
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
    "  `minibar` enum('N','Y') NOT NULL,"
    "  PRIMARY KEY (`room_id`), UNIQUE KEY `room_no` (`room_no`)"
    ") ENGINE=InnoDB")

TABLES['booking'] = (
    "CREATE TABLE `booking` ("
    "  `booking_no` int NOT NULL AUTO_INCREMENT,"
    "  `client_no` int NOT NULL,"
    "  `user_name` varchar(11) NOT NULL,"
    "  `client_fname` varchar(20) NOT NULL,"
    "  `client_lname` varchar(50) NOT NULL,"
    "  `email` varchar(50),"
    "  `phone` varchar(11),"
    "  `room_no` int(3) NOT NULL,"
    "  `check_in` date NOT NULL,"
    "  `check_out` date NOT NULL,"
    "  PRIMARY KEY (`booking_no`), UNIQUE KEY `check_in` (`check_in`), UNIQUE KEY `check_out` (`check_out`),"
    "  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`client_no`) REFERENCES `user` (`client_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`user_name`) REFERENCES `user` (`user_name`) ON DELETE CASCADE,"
    "  CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`email`) REFERENCES `user` (`email`) ON DELETE CASCADE,"
    "  CONSTRAINT `booking_ibfk_4` FOREIGN KEY (`room_no`) REFERENCES `room` (`room_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")


    
# Create a connection object ------------------------------------------------------------------------------------------------------------------
Host = "localhost"                     # IP address of the MySQL database server 
User = "root"                          # User name of the database server 
Password = "microsoftSurface"          # Password for the database user 
connection = pymysql.connect(host=Host, user=User, password=Password) 

# Create a cursor object 
cursor = connection.cursor() 



# Create HWB Hotels Schema --------------------------------------------------------------------------------------------------------------------
## Create database
cursor.execute("DROP DATABASE {}".format(DB_NAME))
print("*------------------------------------*")
print('Existing database dropped!')
print("*------------------------------------* \n\n")

try:
    with connection.cursor() as cur:
        cur.execute("CREATE DATABASE HWBHotels")
        print('Created database: {}'.format(DB_NAME))
except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
print("-------------------------------------")

## Create tables
print("Creating tables...")
connection = pymysql.connect(host=Host, user=User, password=Password, db=DB_NAME) 
cursor = connection.cursor() 

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table [{}]: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
            print(err.msg)
    else:
        print("OK")
print("\n-------------------------------------")

## Creating table entries
today = datetime.now().date()
add_user = ("INSERT INTO user "
               "(user_name, password, first_name, last_name, birth_date, email, phone, creation_date) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
admin_user = ('Admin_User', '1234abcd1234', 'Tina', 'Snow', date(1995, 2, 15), 'tina_snow@admin.com', 14169670000, today)
test_user_1 = ('TestUserOne', '1234abcd1235', 'TestOne', 'UserOne', date(1985, 5, 8), 'test_user1@abc.com', 14169671111, today)
test_user_2 = ('TestUserTwo', '1234abcd1236', 'TestTwo', 'UserTwo', date(2001, 11, 28), 'test_user2@abc.com', 14169672222, today)
cursor.execute(add_user, admin_user)
cursor.execute(add_user, test_user_1)
cursor.execute(add_user, test_user_2)

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
penthouse = ('Toronto', 1, 401, 'Y', 6, 'Y', 'Jacuzzi Tub', 'Y')
cursor.execute(add_room, room101)
cursor.execute(add_room, room102)
cursor.execute(add_room, room103)
cursor.execute(add_room, room201)
cursor.execute(add_room, room202)
cursor.execute(add_room, room203)
cursor.execute(add_room, room301)
cursor.execute(add_room, room302)
cursor.execute(add_room, room303)
cursor.execute(add_room, penthouse)

# checkin1 = datetime.date(2024, 3, 15)
# checkout1 = datetime.date(2024, 3, 21)
# checkin2 = datetime.date(2024, 6, 11)
# checkout2 = datetime.date(2024, 6, 21)
add_booking = ("INSERT INTO booking "
               "(client_no, user_name, client_fname, client_lname, room_no, check_in, check_out) "
               "VALUES (%(client_no)s, %(user_name)s, %(client_fname)s, %(client_lname)s, %(room_no)s, %(check_in)s, %(check_out)s)")
# checkin1 = '2024-03-15'
# checkout1 = '2024-03-21'
# checkin2 = '2024-06-11'
# checkout2 = '2024-06-21'
# checkin1 = pandas.to_datetime('2024/3/15', 'yyyy/mm/dd')
# checkout1 = to_datetime('2024/3/21', 'yyyy/mm/dd')
# checkin2 = to_datetime('2024/5611', 'yyyy/mm/dd')
# checkout2 = to_datetime('2024/6/21', 'yyyy/mm/dd')
checkin1 = date(2024, 3, 15)
checkout1 = date(2024, 3, 21)
checkin2 = date(2024, 6, 11)
checkout2 = date(2024, 6, 21)
# ck1 = checkin1.strftime('%Y-%m-%d %H:%M:%S')
# co1 = checkout1.strftime('%Y-%m-%d %H:%M:%S')
# ck2 = checkin2.strftime('%Y-%m-%d %H:%M:%S')
# co2 = checkout2.strftime('%Y-%m-%d %H:%M:%S')
#booking1 = ('1234abcd1235', 'TestOne', 'UserOne', 101, date(2024, 3, 15), date(2024, 3, 21))
#booking2 = ('1234abcd1236', 'TestTwo', 'UserTwo', 303, date(2024, 6, 11), date(2024, 6, 21))
# booking1 = ('1234abcd1235', 'TestOne', 'UserOne', 101, '2024-03-15', '2024-03-15')
# booking2 = ('1234abcd1236', 'TestTwo', 'UserTwo', 303, checkin2, checkout2)
booking1 = {
    'client_no': 2,
    'user_name': 'TestUserOne',
    'client_fname':'TestOne', 
    'client_lname':'UserOne', 
    'room_no':101, 
    'check_in':'2024-03-15', 
    'check_out':'2024-03-15'}
#booking2 = ('1234abcd1236', 'TestTwo', 'UserTwo', 303, checkin2, checkout2)
# booking1 = ('1234abcd1235', 'TestOne', 'UserOne', 101, ck1, co1)
# booking2 = ('1234abcd1236', 'TestTwo', 'UserTwo', 303, ck2, co2)
cursor.execute(add_booking, booking1)
#cursor.execute(add_booking, booking2)





# Show entries in server -----------------------------------------------------------------------------------------------------------------
## Show all databases
cursor.execute("SHOW DATABASES")       # SQL command      
databaseList = cursor.fetchall()       # Fetch all objects [databases] in cursor
print("Listing all databases in server ...")
for database in databaseList:          # For every database in database list variable   
    print("- {}".format(database))                    # Print to Console each one
print("\n-------------------------------------")
   
## Show all tables in HWB Hotels DB
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'HWBHotels'")
tableList = cursor.fetchall()
print("Listing all the tables in {} database ...".format(DB_NAME))
for table in tableList:
    print("- {}".format(table))                    # Print to Console each one
print("\n-------------------------------------")
    
## Show entries in user table
print('Users - Name List:')
cursor.execute("SELECT client_no, first_name, last_name FROM HWBHotels.user")
clientno = cursor.fetchall()
for client in clientno:
    print("- {}".format(client))
print("\n-------------------------------------")

## Show entries in room table
print("Listing all rooms in HWB Hotels [Toronto Location] ...")
cursor.execute("SELECT floor_no, room_no, bed_no FROM HWBHotels.room")
roomList = cursor.fetchall()
for room in roomList:
    print("- {}".format(room))
print("\n-------------------------------------")

## Show entries in booking table
print("Listing all bookings for HWB Hotels [Toronto Location] ...")
cursor.execute("SELECT booking_no, client_no, room_no, check_in, check_out FROM HWBHotels.booking")
bookingList = cursor.fetchall()
for booking in bookingList:
    print("- {}".format(booking))
print("\n-------------------------------------")

## Closing message
print("HWB Hotels database has officially been set-up & populated with \nsample data!\nConnection to server will now close. Goodbye.\n")


## Close connection
cursor.close()
connection.close()                     
