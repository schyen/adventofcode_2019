# Advent of code - Day 3

import pandas as pd
import numpy as np 
import re
from scipy.spatial import distance
import itertools
from shapely.geometry import MultiLineString

# read in data
wires = open("day03.txt", "r").readlines()

# put each wire into a list -- panel is list of wires
panel = []
for w in wires:
    
    wire = w.strip('\n').split(',')
    
    # initialize coordinates with origin
    lines = []
    
    # going through one coordinate at a time
    for i, step in enumerate(wire):
        if i == 0:
            ref_coord = (0,0)
        else:
            ref_coord = entry_coord
        
        x_val = int(ref_coord[0])
        y_val = int(ref_coord[1])
        
        # parse coordinate so L/R changes x and U/D changes y
        pattern = re.compile("^(L|R|U|D)(\d+)$")
        match = pattern.search(step)
        plane = match.group(1)
        magnitude = match.group(2)
        magnitude = int(magnitude)
        
        # incrementing coordinate
        if plane in ['L','R']:
            axis = 'x'
            if plane == 'R':
                x_val = x_val + magnitude
                step_dir = 1
            else:
                x_val = x_val - magnitude
                step_dir = -1
        else:
            axis = 'y'
            if plane == 'U':
                y_val = y_val + magnitude
                step_dir = 1
            else:
                y_val = y_val - magnitude
                step_dir = -1
        
        # add coordinate as tuple
        entry_coord = (x_val, y_val)

        # create pairs of coordinates
        coord_pair = (ref_coord, entry_coord)
        lines.append(coord_pair)
        # # create coordinates for all points between ref coord and entry coord
        # if axis == 'x':
        #     dum_x = list(range(ref_coord[0], entry_coord[0], step_dir))
        #     dum_y = np.repeat(y_val, len(dum_x))
        # else:
        #     dum_y = list(range(ref_coord[1], entry_coord[1], step_dir))
        #     dum_x = np.repeat(x_val, len(dum_y))
        
        # for x, y in zip(dum_x, dum_y):
        #     entry = (x, y)
        #     coord.append(entry)        

    # drop origin
    del lines[0]

    # convert coordinate pairs into lines
    entry  = MultiLineString(lines)
    
    # panel is list of wires
    panel.append(entry) 

print(len(panel[0]))
print(len(panel[1]))

# find blue lines that intersect with red lines
keep = []
for red in panel[0]:
    for blue in panel[1]:
        # find when wires intersect
        check = blue.intersects(red)
        if check:
            # store interesecting wires as tuples 
            keep.append((red, blue))

print(len(keep))

# extract line coordinates
red_line = []
blue_line = []
for pair in keep:
    red = pair[0]
    blue = pair[1]
    red_coord = (red.coords[0], red.coords[1])
    blue_coord = (blue.coords[0], blue.coords[1])
    red_line.append(red_coord)
    blue_line.append(blue_coord)

# find points of intersection
xpoint = []
for i, pair in enumerate(keep):
    entry = pair[0].intersection(pair[1])
    xpoint.append(entry)

# calculate manhattan's distance of intersections to origin
origin = (0,0)
mdist = []
for x in xpoint: 
    entry = distance.cityblock(origin, x)
    mdist.append(entry)
print(mdist)
# intersection closest to origin
answer = min(mdist)
print(answer)
