from pprint import pprint
import numpy as np

def expand_universe(map):
    for row in map:
        galaxy_found = False
        for i in row:
            if i == '#':
                print(f"Found galaxy at {row.index(i)+1} in {row}")
                galaxy_found = True
                break
        if not galaxy_found: print(f"Row {row} has no galaxies :(")
    
    for col in range(len(map[0])):
        for row in map:
            print(row[col], end=" ")
        print()
        
            
    

def read_input_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        # Remove newline characters and split each line into individual elements
        np.array = [list(line.strip()) for line in lines]
    return np.array


input_filepath = './Day-11/Day11Cal.txt'
map = read_input_file(input_filepath)
pprint(map)
expand_universe(map)


