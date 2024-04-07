import sqlite3

def create_user_table():
    try:
        with sqlite3.connect('users.db') as conn:
            csr = conn.cursor()
            create_user_table_query = ''' 
            CREATE TABLE IF NOT EXISTS users(
            username VARCHAR(50) PRIMARY KEY,
            password VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL UNIQUE CHECK(email LIKE '%@%.com' OR email LIKE '%@%.net'),
            first_name TEXT(50) NOT NULL,
            last_name TEXT(50) NOT NULL,
            age INT,
            gender CHAR(20) CHECK(gender IN('M', 'F', 'Other')),
            address VARCHAR(50) CHECK(address GLOB '[0-9]* [A-Za-z0-9]*')
            )'''
            csr.execute(create_user_table_query)
    except sqlite3.Error as err:
        print(f'Table Error: {err}')

def create_user_with_profile(username, password, email, first_name, last_name, age, gender, address):
    try:
        with sqlite3.connect('users.db') as conn:
            csr = conn.cursor()
            create_new_user_query = '''
            INSERT INTO users (username, password, email, first_name, last_name, age, gender, address)
            VALUES(?,?,?,?,?,?,?,?)
            '''
            csr.execute(create_new_user_query, (username, password, email, first_name, last_name, age, gender, address))
            # print('User Created')
    except sqlite3.Error as err:
        print(f'{username} Error: {err}')

def retrieve_users_by_criteria(info, criteria):
    try:
        with sqlite3.connect('users.db') as conn:
            csr = conn.cursor()
            query = f'SELECT * FROM users WHERE {info} = ?'
            csr.execute(query, (criteria,))
            output = csr.fetchall()
            return output
    except sqlite3.Error as err:
        print(f'Retrieving Error: {err}')

def update_user_profile(username, info, updated_info):
    try:
        with sqlite3.connect('users.db') as conn:
            csr = conn.cursor()
            if info == 'username':
                update_user_query = '''
                UPDATE users
                SET username = ?
                WHERE username = ?'''
                csr.execute(update_user_query, (updated_info, username))
                conn.commit()
            # print('Update Successful')
    except sqlite3.Error as err:
        print(f'{username} Updating Error: {err}')

def delete_user(username):
    try:
        with sqlite3.connect('users.db') as conn:
            csr = conn.cursor()
            check_user_query = '''SELECT * FROM users WHERE username = ?'''
            csr.execute(check_user_query, (username,))
            existing_user = csr.fetchone()
            if existing_user:
                delete_user_query = '''DELETE FROM users WHERE username = ?'''
                csr.execute(delete_user_query, (username,))
                conn.commit()
                # print(f'Deleted user: {username}')
            else:
                print(f'User {username} does not exist')
    except sqlite3.Error as err:
        print(f'Deleting {username} Error: {err}')


create_user_table()
create_user_with_profile('user5', 'password2', 'user5@example.com', 'Jane', 'Smith', 25, 'F', '456 Elm St')
create_user_with_profile('user9', 'password2', 'user9@example.com', 'Jane', 'Smith', 25, 'F', '456 Elm St')
create_user_with_profile('user6', 'password2', 'user6@example.com', 'Jane', 'Smith', 25, 'F', '1 Elm St')
print(retrieve_users_by_criteria('gender', 'F'))
(retrieve_users_by_criteria('username', 'user9'))
(retrieve_users_by_criteria('username', 'user6'))
update_user_profile('user5', 'username', 'user8')
(retrieve_users_by_criteria('username', 'user5'))
delete_user('user8')
delete_user('user5')

