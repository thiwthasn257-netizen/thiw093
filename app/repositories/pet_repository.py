from app.database.connection import get_connection


def get_all_pets() -> list[dict]:
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM pets ORDER BY id")
            return cursor.fetchall()
        finally:
            cursor.close()
    finally:
        connection.close()


def get_pet_by_id(pet_id: int) -> dict | None:
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM pets WHERE id = %s", (pet_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
    finally:
        connection.close()
