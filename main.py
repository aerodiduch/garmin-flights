import pandas
from datetime import datetime
import re
from libs import kml_converter
from pathlib import Path

OUTPUT_FORMAT = "%a %d %b %y %H:%M"

def sexagesimal_to_decimal(coord):
    """Converts a sexagesimal coordinate to decimal degrees.

    Args:
        coord (str): Sexagesimal coordinate (e.g. 'S34° 40.624' W58° 51.277')

    Returns:
        tuple: A tuple containing the latitude and longitude in decimal degrees.
    """
    matches = re.findall(r"([NSWE])\s*(\d+)°\s*(\d+\.\d+)'", coord)
    decimal_coords = []
    for match in matches:
        direction, degrees, minutes = match
        decimal = float(degrees) + float(minutes) / 60
        if direction in "SW":
            decimal *= -1
        decimal_coords.append(decimal)
    return tuple(decimal_coords)


def is_new_flight(timestamp_1, timestamp_2):
    """Determine if a new flight started by their timestamps.
    Having in mind that the Garmin Aera 500 records a timestamp every
    10 seconds in average, we can set a treshold to determine
    when a new flight starts.

    Timestamp format is DD/MM/YYYY HH:MM:SS

    Args:
        timestamp_1 (datetime.datetime): Initial flight timestamp
        timestamp_2 (datetime.datetime): Secondary flight timestamp

    Returns:
        bool: True if the diff between timestamps is > than 15 minutes
    """

    delta = timestamp_2 - timestamp_1
    if delta.total_seconds() >= 900:
        return True
    return False


def convert_elevation(elevation):
    return int(elevation.split(" ")[0])


def separate_flights(df):
    """Splits flights in a DataFrame into separate DataFrames.

    Data needs to be in a certain format:
        - Column names: INDEX | ELEVATION | LEG DISTANCE | LEG TIME | LEG SPEED | LEG COURSE | TIME | POSITION
        - TIME column must comply with format DD/MM/YYYY HH:MM:SS (e.g. 01/01/2021 12:00:00)
        - POSITION is in sexagesimal format (e.g. 41°24'12.2"N 2°10'26.5"E)
        - ELEVATION is in meters.
        - LEG DISTANCE is in meters.
        - LEG TIME is in HH:MM:SS.
        - LEG SPEED is in km/h.
        - LEG COURSE is in TRUE degrees.

    Args:
        df (pandas.DataFrame): Pandas DataFrame containing rows and columns from Garmin Aera 500.

    """
    df["TIME"] = pandas.to_datetime(df["TIME"], format="%d/%m/%Y %H:%M:%S")
    start_time = df["TIME"][0]
    flights = []
    current_flight = []
    for index, row in df.iterrows():
        if is_new_flight(start_time, row["TIME"]):
            flights.append(pandas.DataFrame(current_flight, columns=df.columns))
            current_flight = []

        current_flight.append(row.tolist())
        start_time = row["TIME"]

    flights.append(pandas.DataFrame(current_flight, columns=df.columns))

    return flights


if __name__ == "__main__":
    df = pandas.read_excel("data.xlsx")
    df["LATITUDE"], df["LONGITUDE"] = zip(*df["POSITION"].apply(sexagesimal_to_decimal))
    df["ELEVATION"] = df["ELEVATION"].apply(convert_elevation)
    flights = separate_flights(df)
    path = Path(f"output/{datetime.now().strftime('Export %d-%m-%Y %H:%M')}")
    path.mkdir(parents=True, exist_ok=True)
    flight_number = 0
    for dataframe in flights:
        data = kml_converter.export_kml(dataframe)
        filename = f'{dataframe['TIME'][0].strftime(OUTPUT_FORMAT)} al {dataframe['TIME'].iloc[-1].strftime(OUTPUT_FORMAT)}'
        with open(path / f"{filename}.kml", "w") as f:
            f.write(data)
        flight_number += 1


# if __name__ == "__main__":
#     df = pandas.read_excel("data.xlsx")
#     df["TIME"] = pandas.to_datetime(df["TIME"], format="%d/%m/%Y %H:%M:%S")
#     start_time = df["TIME"][0]
#     flights = []
#     current_flight = pandas.DataFrame(columns=df.columns)
#     for index, row in df.iterrows():
#         if separate_flight(start_time, row["TIME"]):
#             flights.append(current_flight)
#             current_flight = pandas.DataFrame(columns=df.columns)

#         current_flight = pandas.concat([current_flight, pandas.DataFrame(row).T])

#         start_time = row["TIME"]

#     flights.append(current_flight)
