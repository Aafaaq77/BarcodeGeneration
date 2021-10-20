from sqlalchemy import Column, String, Integer
from base import Base
from check_hash_password import hash_password

class User(Base):
    '''
    Class for the users of the application.
    Connected with the Database --> creates the table for the users.
    Attributes of a user object:
                    user_id: ID, Unique ID of a user.
                    user_name: username to be used for logging in the application.
                    password: password to control the access to the app
    '''

    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)

    def __init__(self, user_name, password):
        '''
        initiating a user object with given username.
        Password will be hashed and then saved in the database.
        '''
        self.user_name = user_name
        self.password = hash_password(password) # generate_and_hash_pass(password) # TODO

