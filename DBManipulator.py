import sqlite3


class DBM:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql_q = "SELECT * FROM sitemenu ORDER BY ID DESC"
        try:
            self.__cur.execute(sql_q)
            res = self.__cur.fetchall()
            return res
        except IOError:
            print("Error reading DB")
        return []

    def get_all_lorems(self):
        try:
            self.__cur.execute('SELECT * FROM loremipsum')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Error getting data from DB" + str(e))
        return []

    def get_one_lorem(self, lorem_id):
        try:
            self.__cur.execute(f'SELECT title, text FROM loremipsum WHERE id = {lorem_id} LIMIT 1')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Error getting data from DB" + str(e))
        return False, False
