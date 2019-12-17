# opcode for advent of code 2019
# init_prog is a list of numbers

import sys
import itertools

# noun, verb, and final value for address 0 are specified in param
def my_program(init_prog, noun=None, verb=None, verbose=False):
    
    # first copy over initial prog
    prog = init_prog

    if noun != None & verb != None:
        
        # changing elements 1 and 2
        index = [1, 2]
        replacement = [noun, verb]
        for (i, r) in zip(index, replacement):
            prog[i] = r

    # evaluate first opcode and parameters
    pos = 0
    output = []
    iternum = 1
    run = TRUE
    # going through program at specified positions
    while run:
        print(iternum)
        print(pos)
        # seperate out opcode from parameter
        instruction = [int(d) for d in map(str, prog[pos])]

        ## opcode always last  2 digits
        opcode = instruction[-2:]
        ## mode are all digits prior to opcode
        mode = instruction[:(len(instruction)-len(opcode))]
        ## if opcode 1 or 2, pad with leading 0 in mode for the 'write instructio'
        if opcode in [1,2]:
            mode_len = len(mode)
            mode = list(itertools.repeat(0,  3-mode_len)) + mode  
        ## for other opcodes, pad with one 0 if no modes detected
        elif len(mode) < 1:
            mode = [0] + mode

        print(mode)
        # run through program sequence by the number of parameters
        step = len(opcode) + len(mode)

        # convert opcode to integer
        opcode = int(''.join(map(str, opcode)))
        
        # extract parameters positions
        par_pos = [i+pos+1 for i,x in enumerate(mode)]

        # reading parameters
        par = [prog[i] for i in par_pos]
        
        # put paramter and mode together as tuple
        par_tuple = []
        for m,p in zip(mode, par):
            par_tuple.append((m,p))

        # parameter values
        par_val = []
        # interpreting one parameter at a time
        for i in par_tuple:

            curr_mode = i[0]
            curr_par = i[1]

            # position mode
            if curr_mode == 0:
                # positions of value based on parameter
                curr_val = int(prog[curr_par])
            elif curr_mode == 1:
                # value is the parameter
                curr_val = curr_par

            # record value
            par_val.append(curr_val)

        # interperate opcode to determine output value and write position
        if opcode == 99:
            print('program halted')
            run = False # halt program
        elif opcode == 1:
            result = par_val[0] + par_val[1]
            r_pos = par_val[2]
        elif opcode == 2:
            result = par_val[0] * par_val[1]
            r_pos = par_val[2]
        elif opcode == 3:
            result = int(input("Enter a number: "))
            r_pos = par_val[0]
        elif opcode == 4:
            result = par_val[0]
            r_pos = None
        else:
            print('unknown opcode')
            result = np.nan
            continue

        # write result to position or return a result
        if r_pos is None:
            print('test result')
            output.append(result)
            print(result)
        else:
            prog[r_pos] = result

        # get position of next set of instructions
        pos = pos + step
        
        # verbose
        if verbose:
            print("opcode: %d" % opcode)
            print("param mode:", end = " ")
            print(mode)
            print("param value:", end = " ")
            print(par_val)
            print("result: %d" % result)

        iternum += 1
    return prog, internum, output
