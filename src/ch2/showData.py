import analysisData as ald
import folium
import os
import sys

sudf = ald.sudf
su_lt_two = sudf[sudf['Beds']<2]

map = folium.Map(location=[40.748817, -73.985428], zoom_start=13)
map.choropleth(geo_data=os.path.dirname(sys.path[0])+ os.path.sep + 'data' + os.path.sep + 'nyc.json',
             data=su_lt_two, columns=['Zip', 'Rent'],
             key_on='feature.properties.postalCode',
             threshold_scale=[1700.00, 1900.00, 2100.00, 2300.00, 2500.00, 2750.00],
             fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Rent (%)',
             reset=True)
map.create_map(path='nyc.html')