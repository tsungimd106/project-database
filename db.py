import mysql.connector
from mysql.connector import Error


class DB():
    __host = '140.131.114.148'
    __user = 'root'
    __dbname = 'db'
    __password = 'ntubimd106'
    __conn = None

    @staticmethod
    def execution(sql):
        try:
            connection = mysql.connector.connect(
                host=DB.__host,
                database=DB.__dbname,
                user=DB.__user,
                password=DB.__password,
                charset="utf8")
            if connection.is_connected():
                # 顯示資料庫版本
                db_Info = connection.get_server_info()
                print("資料庫版本：", db_Info)
                # 執行傳入的sql 指令
                cursor = connection.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return rows

        except Error as e:
            print("資料庫連接失敗：", e)
            cursor.close()
            connection.close()

       
