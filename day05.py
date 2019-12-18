# day 5

# import modules
from opcode import my_program

# read in input data
#raw = np.loadtxt(fname = "day05.txt", delimiter = ',')
with open("day05.txt") as f:
    for line in f:
        raw = line.strip('\n').split(',')

raw = [int(x) for x in raw]

# puzzle 1
result, iternum, answer = my_program(raw, verbose = True)

# print(answer)

# puzzle 2
#example = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
#           1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
#           999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
#example = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
#result, iternum, answer = my_program(example, verbose = True)

print(result[0])
