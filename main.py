from scripts.extract import extract_flights_data, extract_airports_data, extract_weather_data

from scripts.transform import clean_flights_data, clean_airports_data, clean_weather_data, \
    merge_flights_airports, merge_flights_weather, clean_dataset, feature_engineering, create_delay_categories

from scripts.load import save_bronze_layer, save_silver_layer, save_gold_layer

from scripts.analyze import calculate_delay_rate, airline_performance, weather_impact_analysis, \
    airport_congestion_analysis, aircraft_reliability_analysis, delay_by_time_period, global_kpis_analysis

def main():
    # EXTRACT :

    df_flights = extract_flights_data()

    df_weather = extract_weather_data()

    df_airports = extract_airports_data()


    # BRONZE LAYER :

    save_bronze_layer(
        df_flights,
        df_weather,
        df_airports
    )


    # CLEANING :

    df_flights_clean = clean_flights_data(
        df_flights
    )

    df_weather_clean = clean_weather_data(
        df_weather
    )

    df_airports_clean = clean_airports_data(
        df_airports
    )

    # Delete raw datasets after cleaning : 
    del df_flights
    del df_weather
    del df_airports

    # MERGES :

    df_flights_airports = merge_flights_airports(
        df_flights_clean,
        df_airports_clean
    )

    df_merged_all = merge_flights_weather(
        df_flights_airports,
        df_weather_clean
    )


    # FINAL CLEANING :

    dataset = clean_dataset(
        df_merged_all
    )


    # FEATURE ENGINEERING :
    dataset = feature_engineering(
        dataset
    )

    dataset = create_delay_categories(
        dataset
    )


    # SILVER LAYER :
    save_silver_layer(dataset)


    # ANALYTICS :
    delay_rate = calculate_delay_rate(dataset)

    airline_perf = airline_performance(dataset)

    weather_impact = weather_impact_analysis(dataset)

    airport_delays = airport_congestion_analysis(dataset)

    aircraft_analysis = aircraft_reliability_analysis(dataset)

    time_analysis = delay_by_time_period(dataset)

    global_kpis = global_kpis_analysis(dataset)

    # GOLD LAYER : 
    save_gold_layer(airline_perf, weather_impact, airport_delays, aircraft_analysis, time_analysis, global_kpis)


if __name__ == "__main__":
    main()