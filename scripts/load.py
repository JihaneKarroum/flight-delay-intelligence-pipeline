import os

# BRONZE LAYER :
def save_bronze_layer(df_flights, df_weather, df_airports):
    os.makedirs("data/bronze", exist_ok=True)

    df_flights.to_parquet(
        "data/bronze/flights_bronze.parquet",
        index=False
    )

    df_weather.to_parquet(
        "data/bronze/weather_bronze.parquet",
        index=False
    )

    df_airports.to_parquet(
        "data/bronze/airports_bronze.parquet",
        index=False
    )

    print("Bronze layer saved successfully.\n")


# SILVER LAYER :
def save_silver_layer(df_silver):
    os.makedirs("data/silver", exist_ok=True)

    df_silver.to_parquet(
        "data/silver/flights_silver.parquet",
        index=False
    )

    print("Silver layer saved successfully.\n")

# GOLD LAYER :
def save_gold_layer(airline_perf, weather_impact, airport_delays, aircraft_analysis, time_analysis, global_kpis):

    os.makedirs("data/gold", exist_ok=True)

    airline_perf.to_parquet(
        "data/gold/airline_performance.parquet",
        index=False
    )

    weather_impact.to_parquet(
        "data/gold/weather_impact.parquet",
        index=False
    )

    airport_delays.to_parquet(
        "data/gold/airport_congestion.parquet",
        index=False
    )

    aircraft_analysis.to_parquet(
        "data/gold/aircraft_reliability.parquet",
        index=False
    )

    time_analysis.to_parquet(
        "data/gold/delay_by_time.parquet",
        index=False
    )

    global_kpis.to_parquet(
        "data/gold/global_kpis.parquet",
    index=False
    )
    
    print("Gold layer saved successfully.\n")