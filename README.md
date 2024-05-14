# Garmin Flights Parser

Easily extract, separate and visualize your flights. A simple processor for data from Garmin Aera 500.

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

This project aims to help people easily extract the data from Garmin Aera 500 and through a Python script separate the flights, parse and export them into a `.kml` format. This allows importing into Google Earth and visualize the flight in 3D space.

## Installation

### Required dependencies

```txt
et-xmlfile==1.1.0
numpy==1.26.4
openpyxl==3.1.2
pandas==2.2.2
python-dateutil==2.9.0.post0
pytz==2024.1
six==1.16.0
tzdata==2024.1
```

### Installation with virtual environment

1) Clone this repo

```bash
git clone https://github.com/aerodiduch/garmin-flights
```

2) Create venv and install dependencies

```bash
cd garmin-flights && python -m venv venv
```

```bash
source venv/bin/activate && pip install -r requirements.txt
```

## Usage

Before executing `main.py` you need to have a xlsx file containing a specific format with the data extracted from Garmin Aera 500. It is mandatory that the file is named `data.xlsx` for the moment, and so is a specific column arrangement.

`data.xlsx`

| INDEX | ELEVATION | LEG DISTANCE | LEG TIME | LEG SPEED | LEG COURSE  | TIME                | POSITION                  |
| ----- | --------- | ------------ | -------- | --------- | ----------- | ------------------- | ------------------------- |
| 1     | 364 m     | 467 m        | 0:00:11  | 150 km/h  | 124.9° true | 06/11/2022 18:41:08 | S34° 40.624' W58° 51.277' |


Have in mind, the displayed time is in format `DD/MM/YYYY HH:MM:SS`

You can have as many rows as you want, my test were with a file with 5000+ rows. Performance will decrease.

Once the data file is present in the root directory of this repo, you can execute main.py

```bash
python main.py
```

This will generate results in `output/current_datetime`. The criteria for separating flights is a time difference of 15 minutes between legs. 

## Contributing
TODO.

## License
TODO.