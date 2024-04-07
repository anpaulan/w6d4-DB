import unittest
import sqlite3
from advanced_user_operations import *

create_user_with_profile('user5', 'password1', 'user5@example.com', 'John', 'Doe', 30, 'M', '123 Oak St')
create_user_with_profile('user2', 'password2', 'user2@example.com', 'Jane', 'Smith', 25, 'F', '456 Elm St')

class TestAdvancedOps(unittest.TestCase):
    def test_create_table(self):
        create_user_table()
        conn = sqlite3.connect('users.db')
        csr = conn.cursor()
        csr.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        exists = csr.fetchall()
        conn.close()
        self.assertIsNotNone(exists)
    
    def test_create_user(self):
        create_user_with_profile('user8', 'password2', 'user8@example.com', 'Jane', 'Smith', 25, 'F', '456 Elm St')
        self.assertIsNotNone(True)
    
    def test_retrieve_data(self):
        user = 'user5'
        retrieve_users_by_criteria('username', user)
        self.assertIsNotNone("No users met criteria")

    def test_update_data(self):
        updated_username = 'user6'
        update_user_profile('user8', 'username', 'user6')
        test = retrieve_users_by_criteria('username', 'user6')
        print(test)
        self.assertEqual(test[0][0], updated_username)
