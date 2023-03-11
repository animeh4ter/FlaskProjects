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