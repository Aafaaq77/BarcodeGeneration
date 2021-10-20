from sqlalchemy import Column, String, Integer, ForeignKey, DATETIME, CHAR
from sqlalchemy.orm import relationship, backref
from base import Base
from users import User
from datetime import datetime

class PrintJob(Base):
    """
    The class to represent a printing job.
    Connected with database --> creates the table to store job related information.
    Attributes:
            job_id: Unique ID of a Job. No job to be printed twice without special permissions.
            job_code: Alphabetic code to be printed under barcodes.txt
            start: Starting point of digits to be printed.
            end: End of the digits code.
                Example:
                    start: 000001 --> end will be, +1000 --> end: 001000

            execution_time: Timestamp with exact time and date from the execution of the printing job.
            user_id: ID of the user which executed the job (Foreign key)
    """

    __tablename__ = 'print_jobs'

    job_id = Column(Integer, primary_key=True)
    job_code = Column(String)
    start = Column(Integer) # TODO, int like 1, 100 or string like '000001' or complete
                            # first code like 'ABC 00000001 E'

    end = Column(Integer) # TODO, same like start
    last_code = Column(CHAR)
    execution_time = Column(DATETIME)

    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship("User", backref=backref('print_jobs'))

    def __init__(self, job_code: str, start: int, end: int,
                last_code:str, user: User):
        """
        Initiating a print_job object with its complete code (
            job_code + start[till end] + last_code
        )
        , the time when the printing job got executed and the user who authorized the printing.
        """
        self.job_code = job_code
        self.start = start
        self.end = end # TODO 
        self.last_code = last_code
        self.execution_time = datetime.now()
        self.user = user

    