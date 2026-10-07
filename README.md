# Garmin Flights

[![License: MIT](https://img.shields.io/github/license/aerodiduch/garmin-flights)](LICENSE) ![Python](https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white) ![Garmin Aera 500](https://img.shields.io/badge/GPS-Garmin%20Aera%20500-007CC3) ![KML for Google Earth](https://img.shields.io/badge/output-KML%20for%20Google%20Earth-34A853)

[Español](README.es.md)

![A handheld aviation GPS on the panel of a small plane at sunset, next to a laptop showing the flight track in Google Earth](docs/cover.jpg)

Extract, separate and see your flights. Garmin Flights takes the data you pull out of a Garmin Aera 500, splits it into one file per flight and writes each flight as a KML track you can open in Google Earth.

- Reads the data from an Excel file (`data.xlsx`).
- A new flight starts whenever there are 15 minutes or more between two points.
- Each flight becomes a KML with the time, position and altitude of every point, named after its start and end time.

## Install

You need Python 3 and Git.

```sh
git clone https://github.com/aerodiduch/garmin-flights
cd garmin-flights
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Put the data in the repo folder as `data.xlsx`, with these columns:

   | INDEX | ELEVATION | LEG DISTANCE | LEG TIME | LEG SPEED | LEG COURSE | TIME | POSITION |
   |---|---|---|---|---|---|---|---|
   | 1 | 364 m | 467 m | 0:00:11 | 150 km/h | 124.9° true | 06/11/2022 18:41:08 | S34° 40.624' W58° 51.277' |

   `TIME` goes as `DD/MM/YYYY HH:MM:SS`, `ELEVATION` in meters and `POSITION` in degrees and decimal minutes.
2. Run:

   ```sh
   python main.py
   ```

3. The KML files land in `output/Export <date and time>/`, one per flight. Open them in Google Earth.

It has handled files of more than 5,000 rows; big files take longer.

## If something doesn't work

- **Windows.** The output folder name includes the time with a colon (for example `13:07`), and Windows doesn't allow colons in folder names. As it is, it runs on macOS and Linux.
- **File not found.** The data has to be called `data.xlsx` and sit next to `main.py`.

## How it works

`main.py` reads the Excel with pandas and turns each position into decimal degrees and each elevation into a number (`libs/parsers.py`). Then it walks the points in order and starts a new flight after a gap of 15 minutes or more. `libs/kml_converter.py` writes each flight as a `gx:Track`, with a `<when>` and a `<gx:coord>` per point.

## License

MIT, see [LICENSE](LICENSE).
