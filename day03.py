# Advent of code - Day 3

import pandas as pd
import numpy as np 
import re
from scipy.spatial import distance
import itertools

# read in data
wires = open("day03.txt", "r").readlines()

# put each wire into a list -- panel is list of wires
panel = []
for w in wires:
    
    wire = w.strip('\n').split(',')
    
    # initialize coordinates with origin
    coord = [(0,0)]
    print(wire[0:5])
    # going through one coordinate at a time
    for i, step in enumerate(wire):
        ref_coord = coord[i]
        x_val = ref_coord[0]
        y_val = ref_coord[1]
        
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
        
        # create coordinates for all points between ref coord and entry coord
        if axis == 'x':
            dum_x = list(range(ref_coord[0], entry_coord[0], step_dir))
            dum_y = np.repeat(y_val, len(dum_x))
        else:
            dum_y = list(range(ref_coord[1], entry_coord[1], step_dir))
            dum_x = np.repeat(x_val, len(dum_y))
        
        for x, y in zip(dum_x, dum_y):
            entry = (x, y)
            coord.append(entry)        
    
    # drop origin
    del coord[0:2]
    coord = set(coord)
    
    # panel is list of wires
    panel.append(coord) 

print(len(panel[0]))
print(len(panel[1]))

# nested loop because wires are different lengths
keep = []
for blue in panel[1]:
    # find when wires intersect
    check = blue in panel[0]
    if check:
        keep.append(blue)

# 
print(len(keep))
# calculate manhattan's distance of intersections to origin
origin = (0,0)
mdist = []
for x in keep: 
    entry = distance.cityblock(origin, x)
    mdist.append(entry)

# intersection closest to origin
answer = min(mdist)
print(answer)
