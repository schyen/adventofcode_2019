# Advent of Code - Day 1

# import modules
import pandas
import numpy as np

# read in data
raw = np.loadtxt(fname = "day01.txt")

# puzzle 1
# convert mass to fuel
## inputs list of mass, outputs list of fuel required for each mass
def calc_fuel(mod_mass):
    fuel = mod_mass / 3
    fuel = np.floor(fuel)
    fuel = fuel - 2
    return fuel

fuel_init = calc_fuel(raw)
tot_fuel = np.sum(fuel_init)
print(tot_fuel)

# puzzle 2
# account for weight of fuel
## going through one module at a time
tot_fuel = []
for i in fuel_init:
    ## fuel needed for initial fuel weight
    fuel_weight = i
    additional_fuel = [fuel_weight]

    while fuel_weight > 0:
        # calculate fuel for fuel weight
        entry = calc_fuel(fuel_weight)
        additional_fuel.append(entry)
        
        # update fuel weight
        fuel_weight = entry
     
    # retrieving positive values
    module_fuel = [i for i in additional_fuel if i > 0]
    module_fuel = np.sum(module_fuel)
    
    # total fuel required for current module
    tot_fuel.append(module_fuel)

# adding up additional fuel required
print(tot_fuel)
print(np.sum(tot_fuel))
