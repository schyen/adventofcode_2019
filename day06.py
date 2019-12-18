# day 06

# load packages

# read input data
data = []
with open("day06.txt") as f:
    for line in f:
        raw = line.strip('\n')
        entry = raw.split(')')
        entry = (entry[0], entry[1])
        data.append(entry)
print(data[0:5])

# function to find orbital path
def find_orbit_path(obj, end):
    # find orbital pair where object is orbiting
    term_pair = [x for x in data if x[1] == obj]
    
    orbit_path = [term_pair[0][1]]
    centre_obj = term_pair[0][0]

    # count number of iterations
    iternum = 0
    # follow orbital pairs down to COM
    while centre_obj != end:
        iternum += 1
        # add centering object to orbit path
        orbit_path.append(centre_obj)
        
        # find pair where centre_obj is doing the orbiting
        curr_pair = [x for x in data if x[1] == centre_obj]
    
        # reset new centre object
        centre_obj = curr_pair[0][0]
        
    return orbit_path

# puzzle 1

# find all unique objects
obj = []
for i in data:
    obj.append(i[0])
    obj.append(i[1])
obj_set = set(obj)
obj_set -= {'COM'}
# sort alphabetically to maintain order
obj_set = sorted(list(obj_set))

# looking at one object at a time
# tot_orb = []
# for obj in obj_set:
#     orbit_path = find_orbit_path(obj, end = 'COM')

#     # count number of direct and indirect orbits in current orbital path
#     n_orb = len(orbit_path)
#     tot_orb.append(n_orb)
    
# answer = sum(tot_orb)
# print(answer)

# puzzle 2

# find orbit path of YOU to COM and SAN to COM
you_com = find_orbit_path('YOU', 'COM')
san_com = find_orbit_path('SAN', 'COM')

# find centre object for YOU and SAN
you_centre = [x[0] for x in data if x[1] == 'YOU']
san_centre = [x[0] for x in data if x[1] == 'SAN']

print(you_centre)
print(san_centre)
# find where they intersect
orb_int = [x for x in you_com if x in san_com]

# intersection that is furthest away from  COM
orb_int = orb_int[0]

# find number of orbits to get to intersection or both orbital paths
you_int = find_orbit_path(you_centre[0], orb_int)
san_int = find_orbit_path(san_centre[0], orb_int)
print(orb_int)
print(you_int[0:5], end = '...')
print(you_int[-5:])
print(san_int[0:5], end = '...')
print(san_int[-5:])
answer = len(you_int) + len(san_int)
print(answer)
