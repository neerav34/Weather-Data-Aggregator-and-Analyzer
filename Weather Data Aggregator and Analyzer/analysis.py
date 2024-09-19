import sqlite3

def calculate_statistics():
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()

    # Average temperature
    cursor.execute("SELECT AVG(temperature) FROM weather")
    avg_temperature = cursor.fetchone()[0]

    # Average humidity
    cursor.execute("SELECT AVG(humidity) FROM weather")
    avg_humidity = cursor.fetchone()[0]

    # Average wind speed
    cursor.execute("SELECT AVG(wind_speed) FROM weather")
    avg_wind_speed = cursor.fetchone()[0]

    connection.close()
    return avg_temperature, avg_humidity, avg_wind_speed
