import pymysql

class DB:
    def getConnection():
        try:
            connection = pymysql.connect(
                host="localhost",
                db="gutara_chat",
                user="admin",
                password="fteam",
                charset="utf8",
                cursorclass=pymysql.cursors.Dictcursor
            )

        except Exception as e:
            print(e + "が発生しています")

        finally:
            return connection
