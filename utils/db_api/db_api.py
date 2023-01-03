import sqlite3


class DataBaseManager:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    async def connect(self, db_name):
        self.__connection = sqlite3.connect(f"{db_name}.db")
        self.__cursor = self.__connection.cursor()

    async def disconnect(self):
        self.__cursor.close()
        self.__connection.close()

    async def get_info(self, get_what, get_from):
        self.__cursor.execute(f"SELECT {get_what} FROM {get_from}")
        return self.__cursor.fetchall()

    async def add_new_info(self, table_name, info):
        self.__cursor.execute(f"INSERT INTO {table_name} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );", info)
        self.__connection.commit()

