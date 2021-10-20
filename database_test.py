from datetime import datetime
from base import Session, engine, Base

from users import User
from print_jobs import PrintJob
from mich_barcodes import generate_barcodes
from check_hash_password import check_password, hash_password

def create_user(user_name, password):
    return User(user_name, password)

def create_printjob(job_code, start, total_count, last_code, user):
    return PrintJob(job_code, start, start+total_count-1, last_code, user)
    

if __name__ == '__main__':
    # Generates Database Schema
    Base.metadata.create_all(engine)

    # Create a new session
    session = Session()

    # Create objects for testing database
    muster_1 = User('muster335', password='my_defaut_pass') # passwd from .txt or another way and default?
    muster_2 = User('muster442', password='strong123')

    bar_job1 = PrintJob('ABC', 1, 1000, 'E', muster_1)
    bar_job2 = PrintJob('ABC', 1001, 2000, 'E', muster_1)
    bar_job3 = PrintJob('AAE', 1, 1000, 'D', muster_2)
    
    # Persisting data
    session.add(muster_1)
    session.add(muster_2)
    session.add(bar_job1)
    session.add(bar_job2)
    session.add(bar_job3)

    # commit and close the session
    session.commit()
    session.close()

    