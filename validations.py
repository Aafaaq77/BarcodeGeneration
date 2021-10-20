# imports
from base import Session, engine, Base

from mich_barcodes import get_codes_from_job
from users import User
from print_jobs import PrintJob
from check_hash_password import check_password, hash_password
from mich_barcodes import get_codes_from_job
from os import remove   

session = Session()


def validate_user(user):
    '''
    Accepts the username as user.
    returns True if user exists in Database. 
    returns False otherwise
    '''
    user_find = session.query(User).filter(User.user_name == user).all()
    if user_find:
        return True
    
    return False
    

def validate_pass(user, password_entered):
    '''
    Cheks if the right password is given for the given user.
    returns True, if password is correct.
    returns False otherwise
    '''
    user_find = session.query(User).filter(User.user_name == user).all()
    right_pass_hash = user_find[0].password
    pass_correct = check_password(password_entered, right_pass_hash)
    if pass_correct:
        with open('user.txt', 'w') as user_file:
            user_file.write(user)
        return True

    return False

def check_job(start_code, start, quantity, end_code):
    '''
    Checks if the job already exists in the datbase.
    Returns True, if there is no job with given parameters.
    Returns False otherwise.
    '''
    not_valid_job = session.query(PrintJob).filter(PrintJob.job_code==start_code
                                    and PrintJob.start==start and PrintJob.end==start+quantity
                                    and PrintJob.last_code==end_code)
    if not_valid_job:
        return False

    return True


def gen_codes(start_code, start, quantity, end_code):
    codes = get_codes_from_job(PrintJob(start_code, start, start+quantity,
                    end_code, User('muster335', password='my_defaut_pass')),
                    code_type='code128')
    for row in range(10):
        code_label = ttk.Label(root, text=f"{next(codes)}")
        code_label.grid(row=row+2, column=1)

def get_user():
    with open('user.txt', 'r') as user_file:
        for row in user_file:
            user = row.rstrip()
            
    remove('user.txt')
    return user