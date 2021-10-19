from db import DB

if __name__ == '__main__':
    db = DB()
    print(db.users())
    # db.remove_user(name='Vasya')
    print(db.users())

    db.is_user_registered(name='VaSYa')