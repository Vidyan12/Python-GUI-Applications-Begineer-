# Importing the tkinter module
from tkinter import *
from datetime import date

# Initializing tkinter
root = Tk()

# Setting the width and height of the GUI
root.geometry("700x500")

# Setting the title of the GUI
root.title("Age Calculator")

# Defining a function to calculate age based on user input
def calculateAge():
    # Storing today's date in the "today" variable
    today = date.today()

    # Getting the birthdate using .get() method
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))

    # Calculating age by subtracting birthdate from today's date
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    # Creating a Label widget to show the calculated age using the grid method
    Label(text=f"{nameValue.get()}, your age is {age}").grid(row=6, column=1)

# Creating label widgets to ask for user information
Label(text="Name").grid(row=1, column=0, padx=90)
Label(text="Year").grid(row=2, column=0)
Label(text="Month").grid(row=3, column=0)
Label(text="Day").grid(row=4, column=0)

# Declaring variables to store user information
nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

# Creating entry widgets to take user information
nameEntry = Entry(root, textvariable=nameValue)
yearEntry = Entry(root, textvariable=yearValue)
monthEntry = Entry(root, textvariable=monthValue)
dayEntry = Entry(root, textvariable=dayValue)

# Placing the entry widgets
nameEntry.grid(row=1, column=1, pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)

# Creating and placing a button to calculate and show age on
# clicking on this button
Button(text="Calculate age", command=calculateAge).grid(row=5, column=1, pady=10)

# Mainloop() is an infinite loop used to run the application when
# it's in ready state
root.mainloop()
