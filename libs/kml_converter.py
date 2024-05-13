import pandas as pd


def convert_to_decimal(coords):
    direction = 1 if coords[-1] in ["N", "E"] else -1
    parts = coords[:-1].split("°")
    degrees = int(parts[0][1:])
    minutes = float(parts[1].split("'")[0])
    decimal = direction * (degrees + minutes / 60)
    return decimal


def convert_elevation(elevation):
    return int(elevation.split(" ")[0])


# Cargar datos desde CSV
data_path = "test1.csv"
data = pd.read_csv(data_path)

# Iniciar el archivo KML como texto
kml_text = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
<Document>
    <open>1</open>
    <visibility>1</visibility>
    <Style id="trackStyle">
        <LineStyle>
            <color>ffDB9034</color>
            <width>4</width>
        </LineStyle>
        <PolyStyle>
            <color>80DB9034</color>
        </PolyStyle>
    </Style>
    <Style id="pathStyle">
        <LineStyle>
            <color>f8000080</color>
            <width>8</width>
        </LineStyle>
    </Style>
    <Style id="positionReportPlacemark">
        <IconStyle>
            <Icon>
                <href>https://maps.google.com/mapfiles/kml/paddle/grn-blank.png</href>
            </Icon>
        </IconStyle>
    </Style>
    <Placemark>
        <styleUrl>#trackStyle</styleUrl>
        <gx:Track>
            <altitudeMode>absolute</altitudeMode>
            <extrude>1</extrude>
            <gx:interpolate>1</gx:interpolate>\n"""

# Agregar coordenadas y tiempos
for index, row in data.iterrows():
    position_parts = row["POSITION"].split(" ")
    lat = position_parts[0] + " " + position_parts[1]
    lon = position_parts[2] + " " + position_parts[3]
    lat_decimal = convert_to_decimal(lat)
    lon_decimal = convert_to_decimal(lon)
    elevation = convert_elevation(row["ELEVATION"])
    timestamp = row["TIME"]
    kml_text += f"            <when>{timestamp}</when>\n            <gx:coord>{lon_decimal} {lat_decimal} {elevation}</gx:coord>\n"

# Finalizar el archivo KML
kml_text += """        </gx:Track>
    </Placemark>
</Document>
</kml>"""

# Guardar el KML como archivo
output_path = "ruta_a_tu_archivo_salida.kml"
with open(output_path, "w") as file:
    file.write(kml_text)

print(f"Archivo KML guardado en {output_path}")
