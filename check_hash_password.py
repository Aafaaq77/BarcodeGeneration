import bcrypt


def hash_password(password: str):
    '''
    Accepts the password (string) as a parameter.
    Returns: hashed_password (string)
    '''
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(
        password, 
        bcrypt.gensalt(10)
        )
    
    return hashed_password.decode()


def check_password(password:str, hashed_password: str):
    '''
    
    '''
    password = password.encode('utf-8')
    hashed_password = hashed_password.encode('utf-8')
    
    return bcrypt.checkpw(password, hashed_password)


if __name__ == '__main__':

    password = 'test_password'
    password_2 = 'testme2'
    hash_1 = hash_password(password)
    hash_2 = hash_password(password_2)
    print(check_password(password, hash_1))
    print(check_password(password_2, hash_2))
    print(check_password(password_2, hash_1))
    print(check_password(password, hash_2))

