import sqlite3

# Initialize the database and create tables if it does not exists
def initialize_database():
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS weather (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        temperature REAL,
                        humidity REAL,
                        wind_speed REAL,
                        timestamp INTEGER
                    )"""
    )
    connection.commit()
    connection.close()


# Save fetched weather data to the database

def save_weather_data(weather_data):
    if weather_data is None:
        print("No weather data to save.")
        return
    try:
        connection = sqlite3.connect("weather_data.db")
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO weather (temperature, humidity, wind_speed, timestamp)
                          VALUES (?, ?, ?, ?)""",
            (
                weather_data["temperature"],
                weather_data["humidity"],
                weather_data["wind_speed"],
                weather_data["timestamp"],
            ),
        )
        connection.commit()
        print("Weather data saved to database.")
    except Exception as e:
        print("Error saving data to database:", e)
    finally:
        connection.close()


# Query data from a specific date range
def query_data(start_date, end_date):
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()
    query = """SELECT * FROM weather WHERE timestamp BETWEEN ? AND ?"""
    cursor.execute(query, (start_date, end_date))
    rows = cursor.fetchall()
    connection.close()
    return rows
