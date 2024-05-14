import re
import pandas


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


def convert_elevation(elevation):
    return int(elevation.split(" ")[0])


def standardize_date(date_str):
    """Standardize date format to 'YYYY-MM-DD HH:MM:SS'

    Args:
        date_str (_type_): _description_

    Returns:
        _type_: _description_
    """

    # Match format 'DD/MM/YYYY HH:MM:SS'
    if re.match(r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}", date_str):
        return pandas.to_datetime(date_str, format="%d/%m/%Y %H:%M:%S")
    # Match format 'YYYY-MM-DD HH:MM:SS'
    elif re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", date_str):
        return pandas.to_datetime(date_str, format="%Y-%d-%m %H:%M:%S")
    else:
        return pandas.NaT
