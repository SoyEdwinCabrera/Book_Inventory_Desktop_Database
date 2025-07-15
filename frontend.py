"""
A program that stores book information:
Title, Author, Year, ISBN

User can:

- View all records
- Search an entry
- Add entry
- Update entry
- Delete entry
- Close the application
"""

from tkinter import * 
import backend  # Import the backend module that handles database operations

# Function to handle the selection of a row in the Listbox
def get_selected_row(event):
    """
    Triggered when a user selects a row in the Listbox.
    Retrieves the selected row's data and populates the input fields with it.
    """
    global selected_tuple
    if list1.curselection():  # Check if a row is selected
        index = list1.curselection()[0]  # Get the index of the selected row
        selected_tuple = list1.get(index)  # Retrieve the data of the selected row
        # Populate the input fields with the selected row's data
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    
# Function to view all records in the database
def view_command():
    """
    Clears the Listbox and populates it with all records from the database.
    """
    list1.delete(0, END)  # Clear the Listbox
    for row in backend.view():  # Fetch all records from the database
        list1.insert(END, row)  # Insert each record into the Listbox
        
# Function to search for specific records in the database
def search_command():
    """
    Searches for records in the database based on user input in the fields.
    Displays the matching records in the Listbox.
    """
    list1.delete(0, END)  # Clear the Listbox
    # Fetch matching records based on user input
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)  # Insert matching records into the Listbox

# Function to add a new record to the database
def add_command():
    """
    Adds a new record to the database using the data entered in the input fields.
    Displays the newly added record in the Listbox.
    """
    # Insert the new record into the database
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)  # Clear the Listbox
    # Display the newly added record in the Listbox
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    
# Function to delete the selected record from the database
def delete_command():
    """
    Deletes the selected record from the database.
    Refreshes the Listbox to reflect the changes.
    """
    backend.delete(selected_tuple[0])  # Delete the record using its ID
    view_command()  # Refresh the Listbox to show updated records
    
# Function to update the selected record in the database
def update_command():
    """
    Updates the selected record in the database with the data entered in the input fields.
    """
    # Update the record in the database using the selected record's ID and new data
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        
# Create the main application window
window = Tk()
window.wm_title("Book Store")  # Set the title of the window

# Create and place labels for the input fields
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Create and place input fields for Title, Author, Year, and ISBN
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# Create and place the Listbox to display records
list1 = Listbox(window, height=6, width=30)
list1.grid(row=2, column=0, rowspan=6, columnspan=2, sticky="nsew")

# Create and place a scrollbar for the Listbox
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, sticky="ns")

# Configure the Listbox and scrollbar to work together
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Bind the Listbox selection event to the get_selected_row function
list1.bind('<<ListboxSelect>>', get_selected_row)

# Create and place buttons for each operation
b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

# Start the main event loop for the application
window.mainloop()
