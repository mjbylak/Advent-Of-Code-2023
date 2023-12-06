import fileinput
import string
from pprint import pprint
import sys
import multiprocessing
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Global Variable Declaration
almanac = []
global debug
debug = False
lowest_from_thread = 0
chunk_size = 1000000
       

def find_location(seed,almanac):
    seed_value = int(seed)
    # if debug: print(f"Checking value {seed}")

    converted = False
    for row in almanac:
        if not row: 
            converted = False
            continue
        elif not isinstance(row[0],int): 
            converted = False
            continue
        elif not converted: 
            if(debug): 
                print("Hopefully looking at this row: ", end = "")
                pprint(row)
        
            base_value = row[1]
            value_range = row[2]
            conversion = row[0]
            
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


def process_chunk(chunk,almanac):
    results = []
    for i in chunk:
        result = find_location(i,almanac)
        results.append(result)
    return results

def main():
    file_name = "Day-5\\Day5.txt"
    # almanac = []
    
    # Handling the first line (seeds)
    first_line = True

    # Creating the seed list to read from
    seed_list = {}

    with open(file_name, "r") as file:
        for line in file:
            if first_line:
                rows = [int(x) if x.isdigit() else x for x in line.split()]
                seed_list = rows
                first_line = False
            else:
                rows = [int(x) if x.isdigit() else x for x in line.split()]
                almanac.append(rows)    

    # pprint(seed_list)
    # pprint(almanac)

    # Call method for finding final seed locations
    pairs = []
    lowest_location = 9999999999999

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []

        for index, seed in enumerate(seed_list):
            if index == 0: continue
            pairs.append(int(seed))
            if (index - 1) % 2:
                if debug:print(f"Inputting seed: {pairs[0]} to {int(pairs[0]) + int(pairs[1])}")
                total_iterations = pairs[1]
                if debug:print(f"Total iterations are {total_iterations}")

                num_chunks = (total_iterations + chunk_size - 1) // chunk_size

                for chunk_num in range(num_chunks):
                    start = chunk_num * chunk_size + pairs[0]
                    end = min((chunk_num + 1) * chunk_size + pairs[0], pairs[0]+total_iterations)
                    print(f"Starting chunk from {start} to {end}")

                    chunk = range(start, end+1)
                    futures.append(executor.submit(process_chunk, chunk, almanac.copy()))


                for future in concurrent.futures.as_completed(futures):
                    results = future.result()
                    if debug: print(f"RESULTS ARE {results}")
                    for result in results:
                        if lowest_location > result:
                            lowest_location = result
                            # print("\nFound lowest location of " + str(lowest_location))


                pairs.clear()

    # Wait for remaining processes to finish
    for future in concurrent.futures.as_completed(futures):
        results = future.result()
        for result in results:
            if lowest_location > result:
                lowest_location = result
                # print("\nFound lowest location of " + str(lowest_location))

    print("\nLowest location value found is " + str(lowest_location))

if __name__ == "__main__":
    main()