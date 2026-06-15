import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Titanum97@",
        database="15-06-db"
    )

def create_weather_table():
    query = """
    CREATE TABLE IF NOT EXISTS records (
    	id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    	name VARCHAR(255) NOT NULL,
    	temperature FLOAT NOT NULL,
    	feels_like FLOAT NOT NULL,
    	wind_speed FLOAT NOT NULL,
    	pressure INT NOT NULL,
    	clouds INT NOT NULL,
    	timestamp DATETIME NOT NULL,
        sunrise DATETIME NOT NULL,
        sunset DATETIME NOT NULL
    );"""

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabela weather została utworzona lub już istnieje")

    except Exception as e:
        print(e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
