# day 04

import itertools
import collections

# input range
lower = 264360
upper = 746325

lower_ls = [int(d) for d in str(lower)]
upper_ls = [int(d) for d in str(upper)]
# rules

# It is a six-digit number
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

myrange  = range(lower, upper)
pool = list(range(0,10))

# first digit must be 2-7 inclusive
prev_digit = [[1],[2],[3],[4],[5],[6],[7]]

# initiate list of potential numbers
candidate_int = []
print(upper)
print(lower)
# work on one digit at a time, starting from second digit
## (first digit determined while selecting candidates for 2nd digit)
for pos in range(1,6):

    print(pos)
    
    # initialize candidates for current digit
    curr_digit = []
        
    # upper and lower bounds of number 
    curr_lower = lower_ls[:pos+1] + list(itertools.repeat(0, 6-(pos+1)))
    lower_int = int(''.join(map(str, curr_lower)))
    
    curr_upper = upper_ls[:pos+1] + list(itertools.repeat(0, 6-(pos+1)))
    upper_int = int(''.join(map(str, curr_upper)))
        
    # prev position has several candidate digits that can't be ruled out until current iteration
    for i, prev  in enumerate(prev_digit):

        # set pool to only include numbers equal to or greater than prev digit
        curr_pool = [x for x in pool if x >= prev[-1]]

        # try each value in the pool for next position
        for digit in curr_pool:
            entry_ls = prev + [digit]
            build_entry = entry_ls + list(itertools.repeat(0, 6-len(entry_ls)))
            entry = int(''.join(map(str, build_entry)))
            
            # keep digits for next iteration
            if lower_int <= entry <= upper_int:
                curr_digit.append(entry_ls)
                
                # keep completed digits for evaluation
                if pos == 5:
                    candidate_int.append(entry)

    # set list of current digits as previous digits for next iteration
    prev_digit = curr_digit

answer = sorted(list(set(candidate_int)))
answer = [x for x in answer if lower <= x <= upper]    

# keeping only integers that have at least one duplicate number
password = []
for i in answer:
    int_as_list = [x for x in str(i)]
    tally = [(k, sum(1 for i in g)) for k,g in itertools.groupby(int_as_list)]
    
    has_double = any([t[1] >= 2 for t in tally]) # puzzle one
    has_double = any([t[1] == 2 for t in tally]) # puzzle two
    if has_double:
        password.append(i)

print(password[:10])
print(password[-10:])
print(len(password))
