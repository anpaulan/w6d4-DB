import sqlite3

class AdvancedUserOperations():
    def create_user_table(self):
        try:
            with sqlite3.connect('users.db') as conn:
                csr = conn.cursor()
                create_user_table_query = ''' 
                CREATE TABLE IF NOT EXISTS users(
                name TEXT(50) NOT NULL,                
                email VARCHAR(50) NOT NULL UNIQUE CHECK(email LIKE '%@%.com' OR email LIKE '%@%.net'),
                password VARCHAR(50) NOT NULL,
                age INT,
                gender CHAR(20) CHECK(gender IN('Male', 'Female', 'Other')),
                address VARCHAR(50) CHECK(address GLOB '[0-9]* [A-Za-z0-9]*')
                )'''
                csr.execute(create_user_table_query)
        except sqlite3.Error as err:
            print(f'Table Error: {err}')

    def create_user_with_profile(self, name, email, password, age, gender, address):
        try:
            with sqlite3.connect('users.db') as conn:
                csr = conn.cursor()
                create_new_user_query = '''
                INSERT INTO users (name, email, password , age, gender, address)
                VALUES(?,?,?,?,?,?)
                '''
                csr.execute(create_new_user_query, (name, email, password , age, gender, address))
                # print('User Created')
        except sqlite3.Error as err:
            print(f'Creating {name} Error: {err}')


    def retrieve_users_by_criteria(self, **kwargs):
        final_qry = list()
        for key, value in kwargs.items():
            if key == 'min_age':
                final_qry.append(f'age >= {value}')
            elif key == 'max_age':
                final_qry.append(f'age <= {value}')
            elif key == 'gender':
                final_qry.append(f'gender = "{value}"')
            elif key == 'email':
                final_qry.append(f'email = "{value}"')
            elif key == 'password':
                final_qry.append(f'password = "{value}"')
            elif key == 'name':
                final_qry.append(f'name = "{value}"')
            elif key == 'address':
                final_qry.append(f'address = "{value}"')

        criteria = ' AND '.join(final_qry)
        try:
            with sqlite3.connect('users.db') as conn:
                csr = conn.cursor()
                query = f'SELECT * FROM users WHERE {criteria}'
                csr.execute(query)
                output = csr.fetchall()
                return output
        except sqlite3.Error as err:
            print(f'Retrieving Error: {err}')

    def update_user_profile(self, email, **kwargs):
        final_qry = list()
        for i, value in kwargs.items():
            if i == 'age':
                final_qry.append(f'age = {value}')
            elif i == 'name':
                final_qry.append(f'name = "{value}"')
            elif i == 'password':
                final_qry.append(f'password = "{value}"')
            elif i == 'gender':
                final_qry.append(f'gender = "{value}"')
            elif i == 'address':
                final_qry.append(f'address = "{value}"')
        
        try:
            with sqlite3.connect('users.db') as conn:
                if final_qry:
                    exec_qry = ', '.join(final_qry)
                    with sqlite3.connect('users.db') as conn:
                        csr = conn.cursor()
                        qry = f'''
                        UPDATE users
                        SET {exec_qry}
                        WHERE email = "{email}"'''
                        csr.execute(qry)
                        conn.commit()
        except sqlite3.Error as err:
            print(f'{email} Updating Error: {err}')
    
    def delete_users_by_criteria(self, **kwargs):
        final_qry = list()
        for i, value in kwargs.items():
            if i == 'age':
                final_qry.append(f'age = {value}')
            elif i == 'name':
                final_qry.append(f'name = "{value}"')
            elif i == 'password':
                final_qry.append(f'password = "{value}"')
            elif i == 'gender':
                final_qry.append(f'gender = "{value}"')
            elif i == 'address':
                final_qry.append(f'address = "{value}"')
        try:
            with sqlite3.connect('users.db') as conn:
                if final_qry:
                    exec_qry = ', '.join(final_qry)
                    with sqlite3.connect('users.db') as conn:
                        csr = conn.cursor()
                        qry = f'''
                        DELETE FROM users WHERE {exec_qry}"'''
                        csr.execute(qry)
                        conn.commit()
        except sqlite3.Error as err:
            print(f'Deleting Error: {err}')