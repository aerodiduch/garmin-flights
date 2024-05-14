import pandas as pd


def export_kml(dataframe, title):
    kml_text = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
<Document>
    <name>{title}</name>
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
    for index, row in dataframe.iterrows():
        lon_decimal = row["LONGITUDE"]
        lat_decimal = row["LATITUDE"]
        timestamp = row["TIME"]
        elevation = row["ELEVATION"]

        kml_text += f"            <when>{timestamp}</when>\n            <gx:coord>{lon_decimal} {lat_decimal} {elevation}</gx:coord>\n"

    kml_text += """        </gx:Track>
    </Placemark>
</Document>
</kml>"""

    return kml_text
