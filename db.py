import mysql.connector
from mysql.connector import Error


class DB():
    @property
    def select(self):
        return 0

    @property
    def create(self):
        return 1

    @property
    def update(self):
        return 2

    @property
    def delete(self):
        return 3

    __host = '140.131.114.148'
    __user = 'root'
    __dbname = 'db'
    __password = 'ntubimd106'
    __conn = None

    @staticmethod
    def execution(type, sqlstr):
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
                if(type == DB.create):
                    cursor.execute(sqlstr)
                    connection.commit()
                elif(type == DB.select):
                    cursor.execute(sqlstr)
                    rows = cursor.fetchall()
                    return rows
                cursor.close()
                connection.close()
                print("enter close")

        except Error as e:
            print("資料庫連接失敗：", e)
            cursor.close()
            connection.close()

    
