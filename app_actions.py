'''
All the actions of the app as functions.
Creating all required frames and actions when clicking or selecting
available buttons or actions in the app.
'''

from tkinter import *
from tkinter import ttk
from validations import validate_user, validate_pass

root = Tk()

def show_frame(frame):
    '''
    Naviagates the main frame to given frame.
    '''
    frame.tkraise()

def login_click():
    '''
    On click: get username and passwords from their respective text fields
    validate username and password from the database.
    if valid username and valid´password:
        navigate to window to print barcodes
    '''
    user = user_entry.get()
    if user != 'username':
        user_valid = validate_user(user)
        if user_valid:
            password = password_entry.get()
            if password != 'Passwort':
                pass_valid = validate_pass(user, password)
                if pass_valid:
                    show_frame(main_frame)
                    root.title('Michelin Barcodes')
                else:
                    label = ttk.Label(login_frame, text='Wrong Password')
                    label.grid(row=9, column=1)
        else:
            label = ttk.Label(login_frame, text='Wrong username')
            label.grid(row=9, column=1)

def create_frames():
    # Frame for login page
    login_frame = ttk.Frame(root)

    # Frame for printing barcodes window
    main_frame = ttk.Frame(root)

    for frame in (main_frame, login_frame):
        frame.grid(row=0, column=0, sticky='nsew')

    show_frame(login_frame)

def create_login_page():
    # filling the left sid eof screen to place widgets in the 2nd column
    for row in range(10):
        label = ttk.Label(login_frame, text='                                             ')
        label.grid(row=row, column=0)

    user_entry = ttk.Entry(login_frame) # Text field to enter username
    user_entry.insert(0, 'username') # default text
    user_entry.grid(row=4, column=1)

    password_entry = ttk.Entry(login_frame) # text field for password
    password_entry.insert(0, 'Passwort')
    password_entry.grid(row=5, column=1, pady=10)

    login = ttk.Button(login_frame, text='Anmelden',
                            command=login_click)
    login.grid(row=7, column=1)
