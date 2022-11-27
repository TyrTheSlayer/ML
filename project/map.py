import matplotlib.pyplot as plt
import geopandas

west = states[states['region'] == 'West']
southwest = states[states['region'] == 'Southwest']
southeast = states[states['region'] == 'Southeast']
midwest = states[states['region'] == 'Midwest']
northeast = states[states['region'] == 'Northeast']
us_boundary_map = states.boundary.plot(figsize=(18, 12), color='Black', linewidth=.5)
west.plot(ax=us_boundary_map,  color="MistyRose")
southwest.plot(ax=us_boundary_map, color="PaleGoldenRod")
southeast.plot(ax=us_boundary_map, color="Plum")
midwest.plot(ax=us_boundary_map, color="PaleTurquoise")
final_map = northeast.plot(ax=us_boundary_map, color="LightPink")