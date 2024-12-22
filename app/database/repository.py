import sqlite3

class BaseRepository:
    pass
    
    
class UserRepository(BaseRepository):
    @classmethod
    def get_users(self):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        users = cur.execute('SELECT * FROM user').fetchall()
        return users
    
    @classmethod
    def get_user(self, email):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        user = cur.execute(f'SELECT * FROM user WHERE email = {email}').fetchall()
        return user
    
    @classmethod
    def get_emails(self):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        emails = cur.execute('SELECT email FROM user').fetchall()
        return emails
    
    @classmethod
    def create_user(self, email, password):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        cur.execute(f'INSERT INTO user(email, password) VALUES({email}, {password})')
        con.commit()
        con.close()
        return
    
    @classmethod
    def delete_user(self, email):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        cur.execute(f'DELETE FROM user WHERE email = {email}')
        con.commit()
        con.close()
        return