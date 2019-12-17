# opcode for advent of code 2019
# init_prog is a list of numbers

# noun, verb, and final value for address 0 are specified in param
def my_program(init_prog, noun=12, verb=2, verbose=False):
    
    # first copy over initial prog
    prog = init_prog
    
    # changing elements 1 and 2
    index = [1, 2]
    replacement = [noun, verb]
    for (i, r) in zip(index, replacement):
        prog[i] = r

    # evaluate first opcode and parameters
    pos = 0

    run = TRUE
    # going through program at specified positions
    while run:

        # seperate out opcode from parameter
        instruction = [int(d) for d in map(str, prog[pos])]

        ## opcode always last  2 digits
        opcode = instruction[-2:]
        ## mode are all digits prior to opcode
        mode = instruction[:(len(instruction)-len(opcode)+1)]
        ## if opcode 1 or 2, pad with leading 0 in mode for the 'write instruction'
        if opcode in [1,2]:
            mode = [0] + mode
            
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
            run = False # halt program
        elif opcode == 1:
            result = par_val[0] + par_val[1]
            r_pos = par_val[2]
        elif opcode == 2:
            result = par_val[0] * par_val[1]
            r_pos = par_val[2]
        elif opcode == 3:
            result = result # result is same result as prev itereration
            r_pos = par_val[0]
        elif opcode == 4:
            result = par_val[0]
            r_pos = par_val[0]
            
        else:
            print('unknown opcode')
            result = np.nan
            continue

        # write result to position
        prog[r_pos] = result
        
        # verbose
        verb_rowname = ['prog','x','y','result']
        verb_colname = ['position','value']
        mat = np.reshape((pos, x_pos, y_pos, r_pos, opcode, x, y, result), (2,4))
        check = pd.DataFrame(mat, verb_colname, verb_rowname)
        if verbose:
            print(check)
    
    return prog, noun, verb
