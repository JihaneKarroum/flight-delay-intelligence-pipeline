import pandas as pd

def extract_flights_data():
    df_flights = pd.read_csv("data/raw/US_flights_2023.csv")
    
    return df_flights

def extract_weather_data():
    df_weather = pd.read_csv("data/raw/weather_meteo_by_airport.csv")
    
    return df_weather

def extract_airports_data():
    df_airports = pd.read_csv("data/raw/airports_geolocation.csv")

    return df_airports