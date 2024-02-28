from __future__ import print_function
from datetime import datetime
import pymysql 
import mysql.connector
from mysql.connector import errorcode
import sys
sys.path.append('C:\\Users\\tahne\\OneDrive\\Desktop\\HWB Hotels\\Models')
from HWBSchema import connection, cursor

## Open connection
Host = "localhost"                     # IP address of the MySQL database server 
User = "root"                          # User name of the database server 
Password = "microsoftSurface"          # Password for the database user 
db = "hwbhotels"
connection = pymysql.connect(host=Host, user=User, password=Password, database=db) 

# Create a cursor object 
cursor = connection.cursor() 

print("Welcome back to HWB Hotels Database")

## Test Queries 

## Test 1 & 2
### Variables
user_varify = 'TestUserOne'
pas_varify = '1234abcd1235'

print("Test 1: Select a row")
sql = "select first_name, last_name, address, birth_date, email, phone from user where user_name = %s and password = %s"
cursor.execute(sql,[(user_varify),(pas_varify)])
results = cursor.fetchall()

user_info_list = list(map(list, results)) ## Convert list of tuples
user_info = user_info_list[0] ## Assign list to variable
fname = user_info[0] ## First name variable

print('{} \n'.format(user_info))

print("Test 2: Get user's first name")
print('{} \n'.format(fname))


### Test 3: Get available rooms between 2024-3-1 to 2024-3-16
print("Test 3: Modify booking table \n- modify client to accept NULL\n- drop foreign keys client_no & email")
try:
    with connection.cursor() as cur:
        sql = (
            "ALTER TABLE `booking` "
            "MODIFY `client_no` int NULL,"
            "DROP FOREIGN KEY `booking_ibfk_1`,"
            "DROP FOREIGN KEY `booking_ibfk_3`"
            )
        cur.execute(sql)
        print("**Booking table has been modified***\n")
        connection.commit()
except mysql.connector.Error as err:
    print("Failed to modify Booking table\n")


## Test 4
print("Test 4: Get available rooms between 2024-3-1 to 2024-3-16")
date1 = datetime(2024, 3, 1)
date2 = datetime(2024, 3, 16)

checkin = date1.date().isoformat()
checkout = date2.date().isoformat()
print(checkin)

formatstring = "- AVAILABLE: Floor #: {0} | Room #: {1} | Split Room: {2} | Bed Amount: {3} | Balconey: {4} | Tub Style: {5} | Minibar: {6}\n"
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
available_options = []
for available in availability:
    option = formatstring.format(*available)
    available_options.append(option)
    print(option)
print(f'Available Options\n {available_options}\n')

print("Okay now I'm done now fr, fr :P\n*------------------------------------*\n")

## Close connection
cursor.close()
connection.close()                     