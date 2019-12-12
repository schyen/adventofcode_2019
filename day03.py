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
delta = []
for w in wires:
    
    wire = w.strip('\n').split(',')
    print(wire[0:5])
    # store steps as lines
    lines = []

    # initialize distance taken with each line
    wire_delta = []
    
    # going through one coordinate at a time
    for i, step in enumerate(wire):
        # initialize coordinates with origin
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
        
        # record number of steps taken with each line
        wire_delta.append(magnitude)

    # drop origin
    del lines[0]

    # convert coordinate pairs into lines
    entry  = MultiLineString(lines)
    print(wire_delta[0:5])
    # panel is list of wires
    panel.append(entry)
    delta.append(wire_delta)


print(len(panel[0]))
print(len(panel[1]))

# find blue lines that intersect with red lines
keep = []
red_line = []
blue_line = []
xpoint = []
x_index = []

for r_i, red in enumerate(panel[0]):
    for b_i, blue in enumerate(panel[1]):
        # find when wires intersect
        check = blue.intersects(red)
        if check:
            # store interesecting wires as tuples 
            keep.append((red, blue))

            # extract line coordinates corresponding to intersecting lines
            red_coord = (red.coords[0], red.coords[1])
            blue_coord = (blue.coords[0], blue.coords[1])
            red_line.append(red_coord)
            blue_line.append(blue_coord)

            # index of lines that intersect
            x_index.append((r_i, b_i))
            
            # find points of intersection
            entry = red.intersection(blue)
            entry = list(entry.coords)
            xpoint.append(entry)

# flatten list of intersection coordinates
xpoint = [i for sublist in xpoint for i in sublist]

# calculate manhattan's distance of intersections to origin
origin = (0,0)
mdist = []
for x in xpoint: 
    entry = distance.cityblock(origin, x)
    mdist.append(entry)
#print(mdist)

# intersection closest to origin
answer = min(mdist)
#print(answer)

# count steps taken by each wire to get to each intersection
x_dist = []
for i, x  in enumerate(x_index):

    # i = ith intersection
    # x = index of (red, blue) wires that intersected

    # number of steps taken to get to intersection
    r_index = x[0] - 1 # subtract 1 because intersection is likely in middle of a line
    b_index = x[1] - 1

    # distance wire travelled to get to intersection (less one line)
    r_dist = sum(delta[0][0:r_index])
    b_dist = sum(delta[1][0:b_index])

    # need to account for distance to intersection on the last line
    # coordinates of last line
    r_last = red_line[i][0]
    b_last = blue_line[i][0]

    # calculate distance from beginning of last line to intersection
    for x,y in zip(r_last, xpoint[i]):
        check = x - y
        if check > 0:
            r_adjust = check
            
    for x,y in zip(b_last, xpoint[i]):
        check = x - y
        if check > 0:
            b_adjust = check
    
    # record total distance both wires took to get to intersection
    entry = r_dist + r_adjust + b_dist + b_adjust
    x_dist.append(entry)

print(x_dist)

answer = min(x_dist)
print(answer)
    
