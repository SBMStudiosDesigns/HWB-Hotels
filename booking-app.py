#Booking App
#Tahnee Pitter-Duncan


from rich.prompt import Prompt
from rich.console import Console
from hotel import  hotel_view

# Variables
available_rooms = 0
welcome_msg = f'\n[black on green] WELCOME TO HWB HOTELS BOOKING APP [/]\n'
available_msg = f'\n[green] We currently have {available_rooms} available to book[/]\n'

# Methods
def starting_room_view():
    room_view = hotel_view[2]
    for i in range(0,4):
        print(room_view*6)


# Main
if __name__ == '__main__':
    console = Console()
    console.print(welcome_msg)
    starting_room_view()
    console.print(available_msg)