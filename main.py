from tkinter import *
from tkinter import ttk
from base import Session, engine, Base
from validations import validate_user, validate_pass, check_job, gen_codes, get_user


# TODO
# Create GUI here.
# Logic of accessing database?
# Default passwords and users


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

def print_onclick():
    '''
    When print button is clicked:
            Gets values from all entry fields (code, start, quantity, end_code).
            Checks if the same job already exists in the database, if it does -> gives warning.
            Generates all the barcodes required for the job.
            Prints all the codes via connected printer.
            Saves the barcode printing job in the database.
    '''
    # start_code = code_entry.get()
    # start = start_entry.get()
    # quantity = quantity_entry.get()
    # end_code = end_code_entry.get()
    # valid_job = check_job(start_code, start, quantity, end_code)
    # if valid_job:
    #     # TODO persisting after creating
    #     gen_codes(start_code, start, quantity, end_code) # 
    # else:
    #     # TODO
    #     # Show label with the warning
    #     pass
    ttk.Label(main_frame, text=get_user()).grid(row=10, column=2)


# setting the root of the App
root = Tk()

root.geometry('470x410')
root.title('Anmelden')

login_frame = ttk.Frame(root)

# Frame for printing barcodes window
main_frame = ttk.Frame(root)

for frame in (main_frame, login_frame):
    frame.grid(row=0, column=0, sticky='nsew')

show_frame(login_frame)

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

# login Page is fully funtional
# TODO
# Registration? or First time Access to the App?

# main page
# filling the left side of screen to place widgets in the 2nd column
for row in range(10):
    label = ttk.Label(main_frame, text='                         ')
    label.grid(row=row, column=0)

code_label = ttk.Label(main_frame, text='Code Eingeben') # code label
code_label.grid(row=3, column=1)

code_entry = ttk.Entry(main_frame) # Entry field for code
code_entry.grid(row=3, column=2, padx=10, pady=10)
ttk.Label(main_frame, text='ABC oder AAE z.B.').grid(row=3, column=3, padx=10)

start_label = ttk.Label(main_frame, text='Anfang') # label for starting number field
start_label.grid(row=4,column=1)

start_entry = ttk.Entry(main_frame) # entry field for starting number
start_entry.grid(row=4, column=2, padx=10, pady=10)
ttk.Label(main_frame, text='1 oder 1001 z.B.').grid(row=4, column=3, padx=10)

quantity_label = ttk.Label(main_frame, text='Anzahl') # label for quantity of labels
quantity_label.grid(row=5,column=1)

quantity_entry = ttk.Entry(main_frame) # entry field for quantity of labels
quantity_entry.grid(row=5, column=2, padx=10, pady=10)
ttk.Label(main_frame, text='"Anfang=1, Anzahl=1000 --> von 00001 bis 01000"').grid(row=5, column=3, padx=10)

end_code = ttk.Label(main_frame, text='Endcode') # label for end code field
end_code.grid(row=6, column=1)

end_code_entry = ttk.Entry(main_frame) # entry field for end code
end_code_entry.grid(row=6, column=2, padx=10)

# Button for printing the codes to the printer
# validates the entries
# checks if the job already exists in the database
# if everything is fine, generates all the codes and then prints
print_button = ttk.Button(main_frame, text='Print',
                            command=print_onclick)

print_button.grid(row=7, column=2, padx=20, pady=10)

root.mainloop()

