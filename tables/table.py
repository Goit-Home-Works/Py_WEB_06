import typing
import logging
from psycopg2 import connect, extensions, Error

column_name = str
column_type = str
foreign_key = str
referencies = str

class Table:
    conn: extensions.connection = None

    def __init__(
        self,
        table_name: str,
        columns: dict[column_name, column_type],
        constrains: list[dict[foreign_key, referencies]]
    ) -> None:
        self.conn = connect(
            dbname="postgres",
            user="postgres",
            password="sergio",
            host="localhost",
            port=5432,
        )

        self.table_name = table_name
        self.columns = columns
        self.constrains = constrains

    def create_table(self) -> int | None:
        full_columns = [f"{key} {val}" for key, val in self.columns.items()]
       
        for constraint in self.constrains:
            pair1, pair2 = constraint.items()
            formatted_constraint = f"{pair1[1]} INTEGER {pair2[0]} {pair2[1]}"
            full_columns.append(formatted_constraint)

        sql_request = (
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ({', '.join(full_columns)});"
        )
        print(sql_request)
        logging.debug(sql_request)

        try:
            c = self.conn.cursor()
            c.execute(sql_request)
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            c.close()


    def get_all(self) -> list[typing.Iterable[typing.Any]] | None:
        rows = None
        cur = self.conn.cursor()

        try:
            cur.execute(f"SELECT * FROM {self.table_name}")
            rows = cur.fetchall()
        except Error as e:
            print(e)
        finally:
            cur.close()

        return rows

    def update(
        self,
        obj_dict: dict[str, typing.Any],
        where_fields: dict[str, typing.Any]
    ):

        obj_str = ", ".join([
            f"{key} = ?"
            for key, value in obj_dict.items()
            if value is not None
        ])

        where_str = ", ".join([f"{i} = ?" for i in where_fields.keys()])

        sql = f'UPDATE {self.table_name} SET {obj_str} WHERE {where_str}'

        logging.debug(sql)

        parameters = [val for val in obj_dict.values() if val is not None]
        parameters.extend(list(where_fields.values()))

        cur = self.conn.cursor()
        try:
            cur.execute(sql, parameters)
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            cur.close()

    def remove(self, where_fields: dict[str, typing.Any]):
        where_str = ", ".join([f"{i} = ?" for i in where_fields.keys()])
        parameters = list(where_fields.values())

        sql = f'DELETE FROM {self.table_name} WHERE {where_str}'

        logging.debug(sql)

        cur = self.conn.cursor()
        try:
            cur.execute(sql, parameters)
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            cur.close()
    def __str__(self):
        return f"{self.__dict__}"
