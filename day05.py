# day 5

# import modules
from opcode import my_program

# read in input data
#raw = np.loadtxt(fname = "day05.txt", delimiter = ',')
with open("day05.txt") as f:
    for line in f:
        raw = line.strip('\n').split(',')

raw = [int(x) for x in raw]
print(raw)
print(len(raw))
# puzzle 1
result, iternum, answer = my_program(raw, verbose = False)

print(answer)
print(result[0])
