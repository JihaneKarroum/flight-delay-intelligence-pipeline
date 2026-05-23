import pandas as pd
import numpy as np

def clean_flights_data(df):
    columns = [
        "FlightDate",
        "Airline",
        "Dep_Airport",
        "Arr_Airport",
        "Dep_CityName",
        "Arr_CityName",
        "DepTime_label",
        "Dep_Delay",
        "Dep_Delay_Type",
        "Arr_Delay",
        "Arr_Delay_Type",
        "Flight_Duration",
        "Distance_type",
        "Delay_Carrier",
        "Delay_Weather",
        "Delay_NAS",
        "Delay_Security",
        "Delay_LastAircraft",
        "Manufacturer",
        "Model",
        "Aicraft_age"
    ]

    df = df[columns].copy()

    df = df.drop_duplicates()

    # Date : 
    df["FlightDate"] = pd.to_datetime(df["FlightDate"])

    # Nulls : 
    df = df.dropna(subset = [
        "Airline",
        "Dep_Airport",
        "Arr_Airport",
        "Dep_Delay",
        "Arr_Delay"
    ])
    

    df = df[df["Flight_Duration"] > 0]

    # optimisation mémoire
    category_columns = [
        "Airline",
        "Dep_Airport",
        "Arr_Airport",
        "Dep_CityName",
        "Arr_CityName",
        "DepTime_label",
        "Dep_Delay_Type",
        "Arr_Delay_Type",
        "Distance_type",
        "Manufacturer",
        "Model"
    ]

    for col in category_columns:
        df[col] = df[col].astype("category")

    return df

def clean_weather_data(df):
    columns = [
        "time",
        "airport_id",
        "tavg",
        "prcp",
        "snow",
        "wspd"
    ]

    df = df[columns].copy()

    df = df.drop_duplicates()

    df["time"] = pd.to_datetime(df["time"])
    
    df = df.dropna(subset = [
        "airport_id",
        "tavg",
        "prcp",
        "snow",
        "wspd"
    ])

    return df

def clean_airports_data(df):
    columns = [
        "IATA_CODE",
        "AIRPORT",
        "CITY",
        "STATE",
        "LATITUDE",
        "LONGITUDE"
    ]
    df = df[columns].copy()

    df = df.drop_duplicates()

    df = df.rename(columns = {
        "AIRPORT" : "Airport_Name"
    })

    df = df.dropna(subset=["IATA_CODE"])

    return df

def merge_flights_airports(df_flights, df_airports):
    df_merged = df_flights.merge(
        df_airports,
        how = "left",
        left_on = "Dep_Airport",
        right_on = "IATA_CODE"    
    ) 

    return df_merged

def merge_flights_weather(df_flights_airports, df_weather):
    df_flights_airports["FlightDate"] = pd.to_datetime(df_flights_airports["FlightDate"]).dt.normalize()
    df_weather["time"] = pd.to_datetime(df_weather["time"]).dt.normalize()
    
    df_merged = df_flights_airports.merge(
        df_weather,
        how = "left",
        left_on = ["Dep_Airport", "FlightDate"],
        right_on = ["airport_id", "time"]
    ) 
    
    return df_merged

def clean_dataset(df_f_a_w):
    df_f_a_w = df_f_a_w.drop(columns=[
    "IATA_CODE",
    "airport_id",
    "time"
    ])

    return df_f_a_w


def feature_engineering(df):

    df = df.copy()

    # delayed flag : 
    df["is_delayed"] = df["Arr_Delay"] > 15

    # total operational delay : 
    df["total_operational_delay"] = (
        df["Delay_Weather"]
        + df["Delay_Carrier"]
        + df["Delay_NAS"]
        + df["Delay_Security"]
        + df["Delay_LastAircraft"]
    )

    # main delay cause :
    delay_columns = [
        "Delay_Weather",
        "Delay_Carrier",
        "Delay_NAS",
        "Delay_Security",
        "Delay_LastAircraft"
    ]

    df["main_delay_cause"] = (
        df[delay_columns]
        .idxmax(axis=1)
    )

    # aircraft age category :
    aircraft_conditions = [
        df["Aicraft_age"] <= 5,
        (df["Aicraft_age"] > 5) & (df["Aicraft_age"] <= 15),
        df["Aicraft_age"] > 15
    ]

    aircraft_choices = [
        "New",
        "Mid-age",
        "Old"
    ]

    df["aircraft_age_category"] = np.select(
        aircraft_conditions,
        aircraft_choices,
        default="Unknown"
    )

    return df

# delay_categories :
def create_delay_categories(df):

    df = df.copy()

    conditions = [
        df["Arr_Delay"] <= 15,
        (df["Arr_Delay"] > 15) & (df["Arr_Delay"] <= 60),
        df["Arr_Delay"] > 60
    ]

    choices = [
        "Low",
        "Medium",
        "High"
    ]

    df["delay_severity"] = np.select(
        conditions,
        choices,
        default="Unknown"
    )

    return df