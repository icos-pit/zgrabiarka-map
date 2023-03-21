#
# # use https://equatorstudios.com/shapefile-viewer to view shape file
# import geopandas as gpd
# import matplotlib.pyplot as plt
# import pandas as pd
# import matplotlib.colors as colors
# import matplotlib as mpl
# import matplotlib.colors as colors
# import folium
# import mapclassify
# import fiona
# import numpy as np
#
#
# if __name__ == '__main__':
#     csv_data_gps = pd.read_csv('data/8/Dane_pozycja_GPS.csv')  # read gps data
#     #TODO: change label to correct names
#     csv_data_gps.columns = ['time', 'lat', 'lat1', 'lat2', 'lat3', 'lon', 'lon1', 'lon2', 'lon3']  # naming columns
#     csv_data = pd.read_csv('data/8/Dane_razem.csv')  # read sensor data
#     csv_data.columns = ['time', 'column1', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7',
#                         'column8']  # naming columns
#
#     csv_data = csv_data[:-1]  # drop the last raw as it's nan
#     csv_data_gps = csv_data_gps[:-1] # drop the last raw as it's nan
#
#     # Convert DMS2DD - degree minute second to degree decimal
#     # data_gps = pd.DataFrame(columns=['latitude', 'longitude', 'height'])
#     # data_gps['latitude'] = csv_data_gps['lat'] + (csv_data_gps['lat1'] / 60) + (csv_data_gps['lat2'] / 3600) + (
#     #         csv_data_gps['lat3'] / 360000 )
#     # data_gps['longitude'] = csv_data_gps['lon'] + (csv_data_gps['lon1'] / 60) + (csv_data_gps['lon2'] / 3600) + (
#     #         csv_data_gps['lon3'] / 360000)
#     #
#     # data_gps['height'] = (csv_data['column3'] * 256) + csv_data['column4'] # Max 658, min 0
#     #
#     #
#     # data_gdf = gpd.GeoDataFrame(data_gps, geometry=gpd.points_from_xy(data_gps['longitude'], data_gps['latitude']))
#     #
#     # # print(data_gdf['color'])
#     #
#     # data_gdf.plot(column='height', cmap=mpl.colormaps['afmhot'], vmin = min(data_gps['height']),
#     #               vmax = max(data_gps['height']), s = 3)
#     #
#     # data_gdf.explore(column='height')
#     # plt.show()
#     # data_gdf.to_file(filename="data.shp", driver='ESRI Shapefile')
#
#
#
#     data_gps = pd.DataFrame(columns=['latitude', 'longitude', 'height'])
#     data_gps['latitude'] = csv_data_gps['lat'] + (csv_data_gps['lat1'] / 60) + (csv_data_gps['lat2'] / 3600) + (
#             csv_data_gps['lat3'] / 360000 )
#     data_gps['longitude'] = csv_data_gps['lon'] + (csv_data_gps['lon1'] / 60) + (csv_data_gps['lon2'] / 3600) + (
#             csv_data_gps['lon3'] / 360000)
#
#     data_gps['height'] = (csv_data['column3'] * 256) + csv_data['column4'] # Max 658, min 0
#
#
#     data = data_gps['height'].values
#     # cmap = mpl.colormaps['RdYlBu']
#     cmap = plt.get_cmap('afmhot')
#     # colors_ = cmap(data)
#     # pose = gpd.points_from_xy(data_gps['longitude'], data_gps['latitude'])
#     # cmap = 'RdYlBu'
#     # norm = colors.Normalize(vmin=data.min(), vmax=data.max())
#     norm = plt.Normalize(vmin=min(data), vmax=max(data))
#     # heatmap = plt.pcolor(pose, cmap=cmap, norm=norm)
#
#     colors_rgb = [cmap(norm(value)) for value in data]
#     # hex_colors = colors.rgb2hex(colors)
#     # print(colors)
#
#     colors_hex = [plt.matplotlib.colors.to_hex(color) for color in colors_rgb]
#
#     data_gdf = gpd.GeoDataFrame(data_gps, geometry=gpd.points_from_xy(data_gps['longitude'], data_gps['latitude']), crs='EPSG:4326')
#
#     # print(data_gdf['color'])
#     data_gdf['Color'] = colors_hex
#     data_gdf.to_file(filename="data.shp", driver='ESRI Shapefile')
#     data_gdf.plot(column='height', cmap=mpl.colormaps['afmhot'], vmin = min(data_gps['height']),
#                   vmax = max(data_gps['height']), s = 3)
#     plt.show()
#
#
#
import random
import shapefile
from geopy.point import Point

# Define the number of GPS coordinates
num_coords = 100

# Define the colors to choose from
colors = ['red', 'green', 'blue', 'yellow']

# Create a new shapefile writer with point shape type
w = shapefile.Writer('gps_coords', shapeType=shapefile.POINT)

# Add a new field called "color" to the shapefile
w.field('color', 'C', 50)

# Loop through the number of GPS coordinates
for i in range(num_coords):
    # Generate a random latitude and longitude
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)

    # Create a new GPS point using the geopy Point class
    point = Point(lat, lon)

    # Set the color attribute for the GPS point
    color = random.choice(colors)

    # Add the GPS point to the shapefile writer with the color attribute
    w.point(lon, lat)
    w.record(color)

# Save the new shapefile
w.save('gps_coords.shp')
