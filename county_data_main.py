import geopandas as gpd
from shapely import wkt
# read in file from shapefile or other format using geopandas
gdf = gpd.read_file('zip://tl_2019_us_county.zip')
gdf = gdf.to_crs(4326)
gdf['geometry'] = gdf.geometry.apply(lambda x: wkt.dumps(x))
# call .to_geoparquet() method on geopandas GeoDataFrame to write to file
gdf.to_parquet('tl_2019_us_county.parquet',compression=None)
#gdf.to_file('dataframe.geojson', driver='GeoJSON')

