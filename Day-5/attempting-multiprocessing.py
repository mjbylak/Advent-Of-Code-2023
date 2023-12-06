import fileinput
import string
from pprint import pprint
import sys
import multiprocessing
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Manager
import concurrent.futures
from multiprocessing import Manager

# Global Variable Declaration
almanac = []
debug = False
lowest_from_thread = 0

nums_per_thread = 1000000

def my_thread(i, result_queue):
    result = find_location(i)
    result_queue.put(result)

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


def process_chunk(chunk):
    results = []
    for i in chunk:
        result = my_thread(i)
        results.append(result)
    return results

def main():
    file_name = "Day-5\\Day5.txt"
    
    # Handling the first line (seeds)
    first_line = True

    # Creating the seed list to read from
    seed_list = {}

    with open(file_name, "r") as file:
        for line in file:
            if first_line:
                rows = [x for x in line.split()]
                seed_list = rows
                first_line = False
            else:
                rows = [x for x in line.split()]
                almanac.append(rows)    

    # Call method for finding final seed locations
    pairs = []
    lowest_location = 9999999999999

    with concurrent.futures.ProcessPoolExecutor() as executor, Manager() as manager:
        result_queue = manager.Queue()

        for index, seed in enumerate(seed_list):
            if index == 0:
                continue
            pairs.append(int(seed))
            if (index - 1) % 2:
                print(f"Inputting seed: {pairs[0]} to {int(pairs[0]) + int(pairs[1])}")

                chunk_size = nums_per_thread
                total_iterations = pairs[1]
                num_chunks = (total_iterations + chunk_size - 1) // chunk_size

                futures = []
                for i in range(pairs[0], pairs[0] + total_iterations):
                    futures.append(executor.submit(my_thread, i, result_queue))

                # Wait for all tasks to complete
                concurrent.futures.wait(futures)

                # Get results from the queue
                while not result_queue.empty():
                    result = result_queue.get()
                    if lowest_location > result:
                        lowest_location = result
                        print("\nFound lowest location of " + str(lowest_location))

                pairs.clear()

            if index > 3:
                break

    print("\nLowest location value found is " + str(lowest_location))

if __name__ == "__main__":
    main()