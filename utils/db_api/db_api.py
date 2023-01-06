import psycopg2


class DataBaseManager:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    async def connect(self):
        self.__connection = psycopg2.connect(
            host="localhost",
            database="requests",
            user="postgres",
            password="463549")

        self.__cursor = self.__connection.cursor()

    async def disconnect(self):
        self.__cursor.close()
        self.__connection.close()

    async def get_info(self, get_what, get_from):
        self.__cursor.execute(f"SELECT {get_what} FROM {get_from}")
        return self.__cursor.fetchall()

    async def add_new_info(self, table_name, info):
        tables = \
            """
            (user_id, 
            user_name, 
            first_name, 
            last_name, 
            selected_address, 
            date, selected_time, 
            persons_name, 
            count_of_guests, 
            phone_number)
            """
        self.__cursor.execute(f"INSERT INTO {table_name} {tables} VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", info)
        self.__connection.commit()

