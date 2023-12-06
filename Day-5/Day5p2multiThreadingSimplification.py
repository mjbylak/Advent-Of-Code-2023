import fileinput
import string
from pprint import pprint
import sys
import multiprocessing
import concurrent.futures

# Global Variable Declaration
almanac = []
debug = False
lowest_from_thread = 0

nums_per_thread = 10000

def my_thread(i):    
    print(i)
    i = find_location(i)
    return i

    # for i in range (1000):
    #     return_value = find_location(pair[i])
        

def find_location(seed):
    seed_value = int(seed)
    if debug: print(f"Checking value {seed}")

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
    pairs = []
    lowest_location = 9999999999999

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for index, seed in enumerate(seed_list):
            if index == 0: continue
            pairs.append(int(seed))
            if (index - 1) % 2:
                print(f"Inputting seed: {pairs[0]} to {int(pairs[0])+int(pairs[1])}")


                for index in range(pairs[1]):
                    i = index+pairs[0]
  
                    futures.append(executor.submit(my_thread, i))

                    for future in concurrent.futures.as_completed(futures):
                        return_value = future.result()
                        if lowest_location > return_value:
                            lowest_location = return_value
                            print("\nFound lowest location of " + str(lowest_location))
                        futures = []

                pairs.clear()

            if index > 3: break

        # Wait for remaining threads to finish
        for future in concurrent.futures.as_completed(futures):
            return_value = future.result()
            if lowest_location > return_value:
                lowest_location = return_value
                print("\nFound lowest location of " + str(lowest_location))

    print("\nLowest location value found is " + str(lowest_location))

if __name__ == "__main__":
    main()