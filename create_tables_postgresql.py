from psycopg2 import connect, extensions, Error
from tables import GradesTable, GroupsTable, StudentsTable, SubjectsTable, TeachersTable


class TableManager:
    def __init__(self, user, password, host, port, dbname):
        self.conn = None
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname

    def connect(self):
        try:
            # Connect to the PostgreSQL server
            self.conn = connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                dbname=self.dbname,
            )
        except Error as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def disconnect(self):
        # Close the connection
        if self.conn:
            self.conn.close()

    def create_tables(self, tables):
        for table in tables:
            table_instance = table()
            table_instance.conn = self.conn
            # print(table_instance)
            table_instance.create_table()


    def make(self, tables):
        self.connect()
        self.create_tables(tables)
        self.disconnect()


if __name__ == "__main__":
    tables_to_create = [
        GradesTable,
        GroupsTable,
        StudentsTable,
        SubjectsTable,
        TeachersTable,
    ]

    table_manager = TableManager(
        user="postgres", password="sergio", host="localhost", port="5432", dbname="postgres",
    )
    table_manager.make(tables_to_create)
