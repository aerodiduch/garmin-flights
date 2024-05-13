import pandas
from datetime import datetime


def separate_flights(timestamp_1, timestamp_2):
    """This functions separates flights by their timestamps.
    Having in mind that the Garmin Aera 500 records a timestamp every
    10 seconds in average, we can set a treshold to determine
    when a new flight starts.

    Timestamp format is DD/MM/YYYY HH:MM:SS

    Args:
        timestamp_1 (datetime.datetime): Initial flight timestamp
        timestamp_2 (datetime.datetime): Secondary flight timestamp
    """

    delta = timestamp_2 - timestamp_1
    if delta.total_seconds() > 900:
        return True
    return False


if __name__ == "__main__":
    df = pandas.read_excel("data.xlsx")
    df["TIME"] = pandas.to_datetime(df["TIME"], format="%d/%m/%Y %H:%M:%S")
    start_time = df["TIME"][0]
    total_flights = 0
    print(start_time)
    for index, row in df.iterrows():
        try:
            if separate_flights(start_time, row["TIME"]):
                print("Flight separated at time: ", row["TIME"])
                total_flights += 1

            start_time = row["TIME"]

        except Exception as e:
            print(e)
            print("Error at row: ", index)
            print(row)

            break
    print(f"total separated flights {total_flights}")
    first_row_datetime = df["TIME"][0]
    last_row_datetime = df["TIME"].iloc[-1]
    total_time = last_row_datetime - first_row_datetime
    print(f"Total time: {total_time}")
