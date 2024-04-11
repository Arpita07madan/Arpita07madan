# Import required modules
from tkinter import *
from tkinter import messagebox
import sqlite3

# Import the code for each component of the system
from vaccine_reservation import *
from vaccine_details import *
from vaccine_admin import *

# Create main window
root = Tk()
root.title("E-Vaccination System")
root.configure(bg='#FADBD8')

# Create a menu bar with options for vaccine reservation, vaccine details and admin access
menubar = Menu(root)
root.config(menu=menubar)
vaccine_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Vaccine Reservation", menu=vaccine_menu)
vaccine_menu.add_command(label="Book a Slot", command=book_slot)
vaccine_menu.add_command(label="Cancel Booking", command=cancel_booking)
vaccine_menu.add_separator()
vaccine_menu.add_command(label="Exit", command=root.quit)

vaccine_details_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Vaccine Details", menu=vaccine_details_menu)
vaccine_details_menu.add_command(label="View Details", command=show_vaccine_details)

admin_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Admin Access", menu=admin_menu)
admin_menu.add_command(label="Add New Vaccine", command=add_vaccine)
admin_menu.add_command(label="Remove Vaccine", command=remove_vaccine)

# Run the main loop
root.mainloop()
