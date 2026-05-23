import pandas as pd

def calculate_delay_rate(df):

    delay_rate = (
        df["is_delayed"].mean() * 100
    )

    print(f"- Delay rate: {delay_rate:.2f}%", '\n')

    return delay_rate

def airline_performance(df):

    airline_perf = (
        df.groupby("Airline").agg({
            "Arr_Delay": "mean",
            "is_delayed": "mean"
        }).reset_index()
    )

    airline_perf = airline_perf.rename(columns={
        "Arr_Delay": "avg_arrival_delay",
        "is_delayed": "delay_rate"
    })

    airline_perf["delay_rate"] = (airline_perf["delay_rate"] * 100)

    airline_perf = airline_perf.sort_values(by="avg_arrival_delay", ascending=False)

    print(airline_perf.head(), '\n')

    return airline_perf

def weather_impact_analysis(df):

    weather_impact = (
        df.groupby("Dep_Airport").agg({
            "Arr_Delay": "mean",
            "prcp": "mean",
            "snow": "mean",
            "wspd": "mean"
        }).reset_index()
    )

    weather_impact = weather_impact.rename(columns={
        "Arr_Delay": "avg_arrival_delay",
        "prcp": "avg_precipitation",
        "snow": "avg_snow",
        "wspd": "avg_wind_speed"
    })

    weather_impact = weather_impact.sort_values(by="avg_arrival_delay", ascending=False)

    print(weather_impact.head(), '\n')

    return weather_impact

def airport_congestion_analysis(df):

    airport_delays = (
        df.groupby("Dep_Airport").agg({
            "Arr_Delay": "mean",
            "is_delayed": "mean"
        }).reset_index()
    )

    airport_delays = airport_delays.rename(columns={
        "Arr_Delay": "avg_arrival_delay",
        "is_delayed": "delay_rate"
    })

    airport_delays["delay_rate"] = (airport_delays["delay_rate"] * 100)

    airport_delays = airport_delays.sort_values(by="avg_arrival_delay", ascending=False)

    print(airport_delays.head(), '\n')

    return airport_delays

def aircraft_reliability_analysis(df):

    aircraft_analysis = (
        df.groupby("aircraft_age_category").agg({
            "Arr_Delay": "mean",
            "is_delayed": "mean"
        }).reset_index()
    )

    aircraft_analysis = aircraft_analysis.rename(columns={
        "Arr_Delay": "avg_arrival_delay",
        "is_delayed": "delay_rate"
    })

    aircraft_analysis["delay_rate"] = (aircraft_analysis["delay_rate"] * 100)

    aircraft_analysis = aircraft_analysis.sort_values(by="avg_arrival_delay", ascending=False)


    print(aircraft_analysis, '\n')

    return aircraft_analysis

def delay_by_time_period(df):

    time_analysis = (
        df.groupby("DepTime_label").agg({
            "Arr_Delay": "mean",
            "is_delayed": "mean"
        }).reset_index()
    )

    time_analysis = time_analysis.rename(columns={
        "Arr_Delay": "avg_arrival_delay",
        "is_delayed": "delay_rate"
    })

    time_analysis["delay_rate"] = (time_analysis["delay_rate"] * 100)
    
    time_analysis = time_analysis.sort_values(by="avg_arrival_delay", ascending=False)

    print(time_analysis, '\n')

    return time_analysis


def global_kpis_analysis(df):
    global_kpis = pd.DataFrame({
        "total_flights": [len(df)],
        "global_delay_rate": [df["is_delayed"].mean() * 100],
        "avg_arrival_delay": [df["Arr_Delay"].mean()]
    })

    return global_kpis