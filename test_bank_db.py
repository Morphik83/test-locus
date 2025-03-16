import sqlite3
import unittest
from bank_db import create_database

class TestBankDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        create_database(self.conn)
        
    def test_user_account_relationship(self):
        c = self.conn.cursor()
        
        # Create a user
        c.execute("INSERT INTO users (username, password) VALUES ('testuser', 'testpass')")
        user_id = c.lastrowid
        
        # Create an account for the user
        c.execute("INSERT INTO accounts (user_id, balance) VALUES (?, 100.0)", (user_id,))
        account_id = c.lastrowid
        
        # Verify relationship
        c.execute("SELECT * FROM accounts WHERE user_id = ?", (user_id,))
        account = c.fetchone()
        
        self.assertIsNotNone(account)
        self.assertEqual(account[1], user_id)
        
    def test_transaction_relationship(self):
        c = self.conn.cursor()
        
        # Create two users and accounts
        c.execute("INSERT INTO users (username, password) VALUES ('user1', 'pass1')")
        user1_id = c.lastrowid
        c.execute("INSERT INTO accounts (user_id, balance) VALUES (?, 100.0)", (user1_id,))
        account1_id = c.lastrowid
        
        c.execute("INSERT INTO users (username, password) VALUES ('user2', 'pass2')")
        user2_id = c.lastrowid
        c.execute("INSERT INTO accounts (user_id, balance) VALUES (?, 50.0)", (user2_id,))
        account2_id = c.lastrowid
        
        # Create a transaction
        c.execute("INSERT INTO transactions (from_account, to_account, amount) VALUES (?, ?, ?)",
                 (account1_id, account2_id, 20.0))
        
        # Verify transaction
        c.execute("SELECT * FROM transactions WHERE from_account = ? AND to_account = ?",
                 (account1_id, account2_id))
        transaction = c.fetchone()
        
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction[3], 20.0)
        
    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
