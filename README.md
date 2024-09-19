# Weather-Data-Aggregator-and-Analyzer
A Python application that fetches weather data from a public API, stores it in a local database, and provides analysis and visualization of the weather trends over time.

## Setup Instructions

1. Create a virtual environment and install dependencies:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt


2. Set up your API key and LOCATION:

    - Open ".env" and replace "YOUR_OWN_API_KEY" with your own API key from [OpenWeatherMap](https://openweathermap.org/),
      and enter your desired "LOCATION".

3. Run the application:

    python main.py


4. Example outputs will include:

    - Average temperature, humidity and wind speed trends in the console.
    - Plots for temperature, humidity and wind speed trends.

## Project Description

This project fetches weather data from a public API, stores it in a local SQLite database, provides basic statistical analysis, and visualizes trends in temperature, humidity and wind speed.



