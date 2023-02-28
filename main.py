# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import wkt
import numpy as np
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csv_data_gps = pd.read_csv('Dane_pozycja_GPS.csv')  # read gps data
    csv_data_gps.columns = ['time', 'lat', 'lat1', 'lat2', 'lat3', 'lon', 'lon1', 'lon2', 'lon3']  # naming columns
    csv_data = pd.read_csv('Dane_razem.csv')  # read sensor data
    csv_data.columns = ['time', 'column1', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7',
                        'column8']  # naming columns

    csv_data = csv_data[:-1]  # drop the last raw as it's nan

    data_gps = pd.DataFrame(columns=['latitude', 'longitude'])
    data_gps['latitude'] = csv_data_gps['lat'] + (csv_data_gps['lat1'] * 0.01) + (csv_data_gps['lat2'] * 0.0001) + (
            csv_data_gps['lat3'] * 0.000001)
    data_gps['longitude'] = csv_data_gps['lon'] + (csv_data_gps['lon1'] * 0.01) + (csv_data_gps['lon2'] * 0.0001) + (
            csv_data_gps['lon3'] * 0.000001)

    data_gps = data_gps[:-1]  # drop the last raw as it's nan

    data_gdf = gpd.GeoDataFrame(data_gps, geometry=gpd.points_from_xy(data_gps['longitude'], data_gps['latitude']))
    this_color_c = []
    for index, raw in data_gdf.iterrows():
        # this_color_c.append('#D94325')
        this_color_c.append(rgb_to_hex((12, 12, 12)))
        print(index)


    data_gdf['color'] = this_color_c
    print(data_gdf['color'])
    data_gdf.plot(color=data_gdf['color'])
    print(data_gdf.plot())
    plt.show()
    print(rgb_to_hex((12, 12, 12)))
    print(rgb_to_hex((12, 12, 12)))
    data_gdf.to_file(filename="data.shp", driver='ESRI Shapefile')
