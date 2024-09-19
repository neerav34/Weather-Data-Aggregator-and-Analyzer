from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve values from .env
API_KEY = os.getenv("API_KEY")
LOCATION = os.getenv("LOCATION")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
