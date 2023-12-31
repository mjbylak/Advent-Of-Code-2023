import fileinput
import string
from pprint import pprint
import sys

# Global Variable Declaration
almanac = []
debug = False

def find_location(seed):
    seed_value = int(seed)

    # Logic is going to take each of the first values in every index of the array unti it finds a [x][y] equal to a number
    # Then it will check the 3rd value [x][2] 
    # Check if the seed value is greater than or equal to the number and less than or equal to the num + [x][2]
    # If so, take the seed num and subtract [x][0] from it, then add that to [x][1] 
    # If not, return the seed 
    # Continue onwards until it finds the next empty array row THEN go past one more and start again
    
    converted = False

    for row in almanac:
        if not row: 
            converted = False
            continue
        elif not row[0].isdigit(): 
            converted = False
            continue
        elif not converted: 
            if(debug): 
                print("Hopefully looking at this row: ", end = "")
                pprint(row)
        
            base_value = int(row[1])
            value_range = int(row[2])
            conversion = int(row[0])
            print(f"Checking row [{conversion},{base_value},{value_range}]")

            if seed_value >= base_value and seed_value <= base_value + value_range:
                print(f"    Converted seed {seed_value} ", end = "")
                temp = seed_value - base_value
                seed_value = conversion + temp
                print(f"to seed_value {str(seed_value)}")
                converted = True
            else: 
                print(f"NOT FOUND IN CONVERSION, CONTINUING AS {seed_value}")
        else: 
            print("WELL SHOOT, HOPEFULLY WE'VE CONVERTED:",seed_value)

    return seed_value


def main():
    
    file_name = "Day-5\\Day5.txt"
    
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

    for index, seed in enumerate(seed_list):
        if index == 0: continue
        print(f"\nInputting seed: {seed}\n")
        if lowest_location > int(find_location(seed)):
            lowest_location = find_location(seed)
            print("\nFound lowest location of " + str(lowest_location))

    print("\nLowest location value found is " + str(lowest_location))

    pass

if __name__ == "__main__":
    main()
