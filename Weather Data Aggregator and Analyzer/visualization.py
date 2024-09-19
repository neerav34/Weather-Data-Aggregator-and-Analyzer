import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime, timezone
import matplotlib.dates as mdates


def visualize_data():
    # Connect to the SQLite database
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()

    # Fetch all weather data from the database
    cursor.execute("SELECT timestamp, temperature, humidity, wind_speed FROM weather")
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    if not data:
        print("No data available for visualization.")
        return

    # Prepare data for plotting
    timestamps = [datetime.fromtimestamp(row[0], tz=timezone.utc) for row in data]
    temperatures = [row[1] for row in data]
    humidity = [row[2] for row in data]
    wind_speed = [row[3] for row in data]

    # Plot Temperature, Humidity, and Wind Speed
    plt.figure(figsize=(10, 8))

    # Temperature Plot
    plt.subplot(3, 1, 1)
    plt.plot(timestamps, temperatures, label="Temperature (°C)", color="r")
    plt.title(f"Weather Data")
    plt.ylabel("Temperature (°C)")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    plt.grid(True) 
    
    # Humidity Plot
    plt.subplot(3, 1, 2)
    plt.plot(timestamps, humidity, label="Humidity (%)", color="b")
    plt.ylabel("Humidity (%)")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    plt.grid(True)
    
    # Wind Speed Plot
    plt.subplot(3, 1, 3)
    plt.plot(timestamps, wind_speed, label="Wind Speed (m/s)", color="g")
    plt.ylabel("Wind Speed (m/s)")
    plt.xlabel("Timestamp")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    plt.grid(True)

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()
