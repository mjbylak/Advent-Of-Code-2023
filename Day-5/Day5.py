import fileinput
import string
from pprint import pprint
import sys

# Global Variable Declaration
almanac = []

def find_location(seed):
    seed_value = int(seed)
    print("Checking value " + seed)

    # Logic is going to take each of the first values in every index of the array unti it finds a [x][y] equal to a number
    # Then it will check the 3rd value [x][2] 
    # Check if the seed value is greater than or equal to the number and less than or equal to the num + [x][2]
    # If so, take the seed num and subtract [x][0] from it, then add that to [x][1] 
    # If not, return the seed 
    # Continue onwards until it finds the next empty array row THEN go past one more and start again
    
    for row in almanac:
        pprint(row)
        if not row or not isinstance(row[0], int): continue

        base_value = int(row[0])
        value_range = int(row[2])
        conversion = int(row[1])

        if seed_value >= base_value and seed_value <= base_value + value_range:
            temp = seed_value - base_value
            seed_value = conversion + temp
            print(seed_value)

    return seed_value


def main():
    
    file_name = "Day-5\\Day5Cal.txt"
    
    # Handling the first line (seeds)
    first_line = True

    # Creating the seeed list to read from
    seed_list = {}

    # NEED AN ARRAY OF 7 ___ height and 3 width
    
    with open(file_name, "r") as file:
        for line in file:

            # First Line Exclusion Logic
            if (first_line):
                rows = [x for x in line.split()]
                seed_list = rows
                first_line = False

            else:
                rows = [x for x in line.split()]
                almanac.append(rows)    

    
    # # Display the resulting array
    # pprint(seed_list)
    # print("\n")
    # pprint(almanac)


    # Call method for finding final seed locations
    lowest_location = 99999999999

    # print(type(lowest_location))
    # print(type(seed_list[2]))

    for i, seed in enumerate(seed_list):
        if i == 0: continue
        if lowest_location > int(find_location(seed)):
            print("Found lowest location of " + str(find_location(seed)) + "\n")
            lowest_location = find_location(seed)

    print(lowest_location)

    pass

if __name__ == "__main__":
    main()
