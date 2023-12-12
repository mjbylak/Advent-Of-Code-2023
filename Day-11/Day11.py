from pprint import pprint
import numpy as np

def print_column(map,j):
    for i in range(len(map)):
        print(map[i][j],end=" ")
    print()

def expand_universe(map):
    
    # for row in map:
    #     galaxy_found = False
    #     for i in row:
    #         if i == '#':
    #             print(f"Found galaxy at {row.index(i)+1} in {row}")
    #             galaxy_found = True
    #             break
    #     if not galaxy_found: print(f"Row {row} has no galaxies :(")
    
    print("\n\n\nStarting Column Mapping")

    # Thinking conceptually, just use the simple 

    # column index is j
    for j in range(len(map[0])):
        galaxy_found = False
        for i in range(len(map)):
            if map[i][j] == '#':
                galaxy_found = True
                print(print_column(map,j),f"Column {j+1} has a galaxy :(")
                break
        # if not galaxy_found: print(f"Column {print_column(map,j)} has no galaxies :(")
        
        
            
    

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


