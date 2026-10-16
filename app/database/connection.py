import os

from dotenv import load_dotenv
import pymysql
from pymysql.connections import Connection

load_dotenv()


def get_connection() -> Connection:
    required_settings = ("DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME")
    missing_settings = [name for name in required_settings if not os.getenv(name)]
    if missing_settings:
        raise RuntimeError(
            f"Missing database configuration: {', '.join(missing_settings)}. "
            "Copy .env.example to .env and configure it."
        )

    try:
        port = int(os.getenv("DB_PORT", "2000"))
    except ValueError as error:
        raise RuntimeError("DB_PORT must be an integer.") from error

    return pymysql.connect(
        host=os.environ["DB_HOST"],
        port=port,
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


if __name__ == "__main__":
    connection = get_connection()
    try:
        print("Connected to MariaDB successfully!")
    finally:
        connection.close()
