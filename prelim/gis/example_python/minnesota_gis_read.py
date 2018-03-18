# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 07:07:17 2018

@author: Zach
"""

import fiona
from shapely import geometry

### Download Shapefile from https://pubs.usgs.gov/of/2004/1355/#MN ####
with fiona.open('C:/Users/Zach/Downloads/MNgeol_dd/mngeol_poly_dd.shp') as fiona_collection:

    for shaper in fiona_collection:

        shape = geometry.asShape( shaper['geometry'] )
    
        point = geometry.Point(-95.4672,46.0047) # longitude, latitude
    
        if shape.contains(point):
            print(shaper['properties']['ROCKTYPE1'],shaper['properties']['ROCKTYPE2'],shaper['properties']['UNIT_AGE'])
            break
