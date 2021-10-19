
class User(object):
    name = ""
    password = ""

    def __init__(self, db_fetch_item):
        #User(1, 'vasya', '111')
        self.name = db_fetch_item[1]
        self.password = db_fetch_item[2]

    def __repr__(self):
        return 'User name: {0}'.format(self.name)