import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            sslmode="require"
        )
        return connection

    except Exception as e:
        print("Database connection error:", e)
        return None