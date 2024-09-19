from weather_data import fetch_weather_data
from database import initialize_database, save_weather_data, query_data
from analysis import calculate_statistics
from visualization import visualize_data
import time

if __name__ == "__main__":
    # Initialize the database

    initialize_database()

    # Fetch and store weather data at regular intervals
    while True:
        weather_data = fetch_weather_data()
        save_weather_data(weather_data)

        # Perform analysis
        avg_temp, avg_humidity, avg_wind_speed = calculate_statistics()
        print(f"Average Temperature: {avg_temp:.2f}°C")
        print(f"Average Humidity: {avg_humidity:.2f}%")
        print(f"Average Wind Speed: {avg_wind_speed:.2f}m/s")

        # Visualize data
        visualize_data()

        # Fetch weather data every hour
        time.sleep(3600) 
