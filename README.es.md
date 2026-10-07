# Garmin Flights

[![License: MIT](https://img.shields.io/github/license/aerodiduch/garmin-flights)](LICENSE) ![Python](https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white) ![Garmin Aera 500](https://img.shields.io/badge/GPS-Garmin%20Aera%20500-007CC3) ![KML for Google Earth](https://img.shields.io/badge/output-KML%20for%20Google%20Earth-34A853)

[English](README.md)

![Un GPS aeronáutico portátil en el panel de un avión chico al atardecer, al lado de una notebook con el track del vuelo en Google Earth](docs/cover.jpg)

Sacá, separá y mirá tus vuelos. Garmin Flights toma los datos que sacás de un Garmin Aera 500, los divide en un archivo por vuelo y escribe cada vuelo como un track KML que podés abrir en Google Earth.

- Lee los datos de un Excel (`data.xlsx`).
- Empieza un vuelo nuevo cada vez que hay 15 minutos o más entre dos puntos.
- Cada vuelo queda en un KML con la hora, la posición y la altitud de cada punto, y lleva de nombre la hora de inicio y de fin.

## Instalación

Necesitás Python 3 y Git.

```sh
git clone https://github.com/aerodiduch/garmin-flights
cd garmin-flights
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Uso

1. Dejá los datos en la carpeta del repo como `data.xlsx`, con estas columnas:

   | INDEX | ELEVATION | LEG DISTANCE | LEG TIME | LEG SPEED | LEG COURSE | TIME | POSITION |
   |---|---|---|---|---|---|---|---|
   | 1 | 364 m | 467 m | 0:00:11 | 150 km/h | 124.9° true | 06/11/2022 18:41:08 | S34° 40.624' W58° 51.277' |

   `TIME` va como `DD/MM/AAAA HH:MM:SS`, `ELEVATION` en metros y `POSITION` en grados y minutos decimales.
2. Corré:

   ```sh
   python main.py
   ```

3. Los KML quedan en `output/Export <fecha y hora>/`, uno por vuelo. Abrilos en Google Earth.

Procesó archivos de más de 5000 filas; los archivos grandes tardan más.

## Si algo no anda

- **Windows.** El nombre de la carpeta de salida lleva la hora con dos puntos (por ejemplo `13:07`), y Windows no acepta dos puntos en los nombres de carpeta. Así como está, anda en macOS y Linux.
- **No encuentra el archivo.** Los datos se tienen que llamar `data.xlsx` y estar al lado de `main.py`.

## Cómo funciona

`main.py` lee el Excel con pandas y pasa cada posición a grados decimales y cada elevación a número (`libs/parsers.py`). Después recorre los puntos en orden y arranca un vuelo nuevo después de un hueco de 15 minutos o más. `libs/kml_converter.py` escribe cada vuelo como un `gx:Track`, con un `<when>` y un `<gx:coord>` por punto.

## Licencia

MIT, ver [LICENSE](LICENSE).
