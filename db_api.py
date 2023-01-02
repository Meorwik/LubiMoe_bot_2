import sqlite3


def check_uniq(funk):
    async def inner_error_check(*args):
        try:
            await funk(*args)
        except sqlite3.IntegrityError:
            pass

    return inner_error_check


class DataBaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    async def connect(self, db_name):
        self.connection = sqlite3.connect(f"{db_name}.db")
        self.cursor = self.connection.cursor()

    async def disconnect(self):
        self.cursor.close()
        self.connection.close()

    async def get_info(self, get_what, get_from):
        self.cursor.execute(f"SELECT {get_what} FROM {get_from}")
        return self.cursor.fetchall()

    @check_uniq
    async def add_new_info(self, table_name, info_format_to_be_added, exact_info):
        print("added______________________")
        self.cursor.execute(f"INSERT INTO {table_name} ({info_format_to_be_added}) VALUES({exact_info})")
        self.connection.commit()

