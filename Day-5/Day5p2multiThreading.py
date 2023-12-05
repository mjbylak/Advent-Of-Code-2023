import fileinput
import string
from pprint import pprint
import sys
import threading

# Global Variable Declaration
almanac = []
debug = False

def my_thread():


def find_location(seed):
    seed_value = int(seed)
    print(f"Checking value {seed}")

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
                if debug: print("Hopefully looking at this row: ", end = "")
                if debug: pprint(row)
        
            base_value = int(row[1])
            value_range = int(row[2])
            conversion = int(row[0])
            if debug: print(f"Checking row [{conversion},{base_value},{value_range}]")

            if seed_value >= base_value and seed_value <= base_value + value_range:
                if debug: print(f"    Converted seed {seed_value} ", end = "")
                temp = seed_value - base_value
                seed_value = conversion + temp
                if debug: print(f"to seed_value {str(seed_value)}")
                converted = True
            else: 
                if debug: print(f"NOT FOUND IN CONVERSION, CONTINUING AS {seed_value}")
        else: 
            if debug: print("WELL SHOOT, HOPEFULLY WE'VE CONVERTED:",seed_value)

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

    # Call method for finding final seed locations
    lowest_location = 99999999999
    pairs = []

    for index, seed in enumerate(seed_list):
        if index == 0: continue
        pairs.append(int(seed))
        if (index-1) % 2:
            if (pairs[0] > pairs[1]):
                temp = pairs[1]
                pairs[1] = pairs[0]
                pairs[0] = temp
            print(f"Inputting seed: {pairs[0]} to {pairs[1]}")
            for i in range (pairs[0], pairs[1]):
                # ADDING MULTITHREADING
                try:
                    x = threading.Thread(target=my_thread, args= (pairs[0], pairs[1]),daemon=True)
                    threads += 1    #thread counter
                    x.start()       #start each thread
                except RuntimeError:    #too many throws a RuntimeError
                    break
                if lowest_location > int(find_location(i)):
                    lowest_location = find_location(i)
                    print("\nFound lowest location of " + str(lowest_location))
            pairs.clear()

    print("\nLowest location value found is " + str(lowest_location))

    pass

if __name__ == "__main__":
    main()