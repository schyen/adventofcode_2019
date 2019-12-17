# day 5

# import modules
import numpy as np
from opcode import my_program

# read in input data
raw = np.loadtxt(fname = "day05.txt", delimiter = ',')

# puzzle 1
myprogram(raw, verbose = True)
