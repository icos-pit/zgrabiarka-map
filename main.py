

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import re

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

    #Convert DMS2DD - degree minute second to degree decimal
    data_gps = pd.DataFrame(columns=['latitude', 'longitude'])
    data_gps['latitude'] = csv_data_gps['lat'] + (csv_data_gps['lat1'] / 60) + (csv_data_gps['lat2'] / 3600) + (
            csv_data_gps['lat3'] / 360000 )
    data_gps['longitude'] = csv_data_gps['lon'] + (csv_data_gps['lon1'] /60 ) + (csv_data_gps['lon2'] / 3600) + (
            csv_data_gps['lon3'] / 360000)

    data_gps = data_gps[:-1]  # drop the last raw as it's nan

    data_gdf = gpd.GeoDataFrame(data_gps, geometry=gpd.points_from_xy(data_gps['longitude'], data_gps['latitude']))




    # print(data_gdf['color'])

    data_gdf.plot()
    plt.show()
    data_gdf.to_file(filename="data.shp", driver='ESRI Shapefile')
