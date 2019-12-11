# Advent of Code - Day 2

# import modules
import pandas as pd
import numpy as np

# puzzle 1
# read in data
# raw = np.loadtxt(fname = "day02.txt", delimiter = ',')

# # first replace values (restore to 1202 program state)
# prog = raw
# index = [1, 2]
# replacement = [12, 2]
# for (i, r) in zip(index, replacement):
    # prog[i] = r

# # run through program sequence by 4s
# prog_pos = range(0, len(prog), 4)

# # going through program at specified positions
# for pos in prog_pos:

    # # check for program 
    # opcode = prog[pos]
    
    # # positions of x and y inputs
    # x_pos = int(prog[pos+1])
    # y_pos = int(prog[pos+2])
    
    # # position of result
    # r_pos = int(prog[pos+3])
 
    # # x and values
    # x = prog[x_pos]
    # y = prog[y_pos]
    
    # if opcode == 99:
        # print('program halted')
        # break
    # elif opcode == 1:
        # result = x + y
    # elif opcode == 2:
        # result = x * y 
    # else:
        # print('unknown opcode')

    # prog[r_pos] = result
    
    # # verbose
    # verb_rowname = ['prog','x','y','result']
    # verb_colname = ['position','value']
    # mat = np.reshape((pos, x_pos, y_pos, r_pos, opcode, x, y, result), (2,4))
    # verb = pd.DataFrame(mat, verb_colname, verb_rowname)
    # #print(verb)

# print(int(prog[0]))

# puzzle 2

# noun, verb, and final value for address 0 are specified in param
def my_program(init_prog, noun=12, verb=2, step = 4, verbose=False):
    
    # first copy over initial prog
    prog = init_prog
    
    # changing elements 1 and 2
    index = [1, 2]
    replacement = [noun, verb]
    for (i, r) in zip(index, replacement):
        prog[i] = r
    
    # run through program sequence by 4s
    prog_pos = range(0, len(prog), step)
    
    # going through program at specified positions
    for pos in prog_pos:
    
        # check for program 
        opcode = prog[pos]
        
        # positions of x and y inputs
        x_pos = int(prog[pos+1])
        y_pos = int(prog[pos+2])
        
        # position of result
        r_pos = int(prog[pos+3])
     
        # x and values
        x = prog[x_pos]
        y = prog[y_pos]
        
        if opcode == 99:
            break
        elif opcode == 1:
            result = x + y
        elif opcode == 2:
            result = x * y 
        else:
            print('unknown opcode')
            result = np.nan
            break

        prog[r_pos] = result
        
        # verbose
        verb_rowname = ['prog','x','y','result']
        verb_colname = ['position','value']
        mat = np.reshape((pos, x_pos, y_pos, r_pos, opcode, x, y, result), (2,4))
        check = pd.DataFrame(mat, verb_colname, verb_rowname)
        if verbose:
            print(check)
    
    return prog, noun, verb

# print(my_program(raw))

# attempt 0-99 for noun and verb (brute force)
brute = range(0,99)


for noun in brute:
    for verb in brute:
        raw = np.loadtxt(fname = "day02.txt", delimiter = ',')
        prog_answer, noun, verb = my_program(init_prog=raw, noun=noun, verb=verb, verbose=False)
        answer = prog_answer[0]
        
        if answer == 19690720:
            break
        
    if answer == 19690720:
            break

print(answer)
print(noun)
print(verb)