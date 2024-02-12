import psycopg2
from psycopg2.extras import RealDictCursor
import logging
import os

# Configure logging
logging.basicConfig(level=logging.ERROR)


def load_config():
    # Your configuration loading logic here
    config = {
        "dbname": "postgres",
        "user": "postgres",
        "password": "sergio",
        "host": "localhost",
        "port": 5432,
    }
    return config


def query_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            query = file.read()
        return query
    except FileNotFoundError as e:
        logging.error(f"Error: File not found - {file_path}: {e}")
        return None



def execute_query(file_path):
    query = query_from_file(file_path)

    # Check if query is not empty
    if query:
        print(f"Executing query from file: {file_path}")
        print("Query:")
        print(query)

        config = load_config()

        conn = psycopg2.connect(
            database=config["dbname"],
            host=config["host"],
            user=config["user"],
            password=config["password"],
            port=config["port"],
        )

        cursor = conn.cursor()
        cursor.execute(query)
        print("Result:")
        print(cursor.fetchall())
        print("\n" + "=" * 50 + "\n")  # Add separator for better readability
    else:
        print(f"Skipping empty or missing query in {file_path}\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    # Get the current working directory
    current_directory = os.getcwd()

    # Specify the relative path to the sql folder
    sql_folder = "sql"

    # List of relative paths to SQL files
    files = [
        "query_01.sql",
        "query_02.sql",
        "query_03.sql",
        "query_04.sql",
        "query_05.sql",
        "query_06.sql",
        "query_07.sql",
        "query_08.sql",
        "query_09.sql",
        "query_10.sql",
        "query_11.sql",
        "query_12.sql",
    ]

    # Create absolute paths by joining current_directory and file paths
    absolute_paths = [
        os.path.join(current_directory, sql_folder, file) for file in files
    ]

    for file_path in absolute_paths:
        print(file_path)
        execute_query(file_path)
