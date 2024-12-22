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
        user = cur.execute(
            f'SELECT * FROM user WHERE email = ?',
            (
                email,
            )
        ).fetchall()
        return user[0]

    @classmethod
    def get_emails(self):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        emails = cur.execute('SELECT email FROM user').fetchall()
        return [email[0] for email in emails]

    @classmethod
    def create_user(self, email, password):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        cur.execute(
            f'INSERT INTO user(email, password) VALUES(?, ?)',
            (
                email,
                password
            )
        )
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


class GiftsRepository(BaseRepository):
    @classmethod
    def get_lists(self):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        lists = cur.execute('SELECT * FROM gifts').fetchall()
        return lists
    
    @classmethod
    def get_list(self, email):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        lists = cur.execute(
            f'SELECT name, count, price, description, isReady FROM gifts WHERE email = ?', 
            (email,)
            ).fetchall()
        return lists

    @classmethod
    def create_list(self, email, name, count, price, description, isReady):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        cur.execute(
            f'INSERT INTO gifts(email, name, count, price, description, isReady) VALUES(?, ?, ?, ?, ?, ?)',
            (
                email,
                name,
                count,
                price,
                description,
                isReady
            )
        )
        con.commit()
        con.close()
        return
    
    @classmethod
    def delete_list(self, email, name, count, price, description, isReady):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        cur.execute(
            f'DELETE FROM gifts WHERE email = ? AND name = ? AND count = ? AND price = ? AND description = ? AND isReady = ? LIMIT 1',
            (
                email,
                name,
                count,
                price,
                description,
                isReady
            )
        )
        con.commit()
        con.close()
        return
    
    @classmethod
    def update_list(self, email, name, count, price, description, isReady, emailNew, nameNew, countNew, priceNew, descriptionNew, isReadyNew):
        con = sqlite3.connect('app/database/database.db')
        cur = con.cursor()
        cur.execute(
            f"""
            UPDATE gifts 
            WHERE email = ? AND name = ? AND count = ? AND price = ? AND description = ? AND isReady = ?
            SET email = ?, name = ?, count = ?, price = ?, description = ?, isReady = ? LIMIT 1
            """,
            (
                email,
                name,
                count,
                price,
                description,
                isReady,
                emailNew,
                nameNew,
                countNew,
                priceNew,
                descriptionNew,
                isReadyNew
            )
        )
        con.commit()
        con.close()
        return
    