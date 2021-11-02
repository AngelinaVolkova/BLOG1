import sqlite3
from user import User
import user


# CRUD - create/read/update/delete
class DB(object):
    def __init__(self):
        self.connection = sqlite3.connect(database='/Users/user/Downloads/BLOG1/test.db')

    # результат - массив юзеров [User]
    def users(self):
        cursor = self.connection.cursor()
        result = cursor.execute('SELECT * from users')
        return list(map(lambda item: User(db_fetch_item=item), result.fetchall()))

    def add_user(self, name, password):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO users(id,name,password) VALUES(?,?,?)', (None, name, password))
        self.connection.commit()

    def remove_user(self, name):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM users WHERE name=?', (name,))
        self.connection.commit()

    def is_user_registered(self, name):
        users = self.users()
        for user in users:
            if name.upper() == user.name.upper():
                print('OK: {0}'.format(user))
