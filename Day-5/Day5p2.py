import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Global Variable Declaration
almanac = []
chunk_size = 1000000
       
def find_location(seed,almanac):
    seed_value = int(seed)

    converted = False
    for row in almanac:
        if not row: 
            converted = False
            continue
        elif not isinstance(row[0],int): 
            converted = False
            continue
        elif not converted: 
        
            base_value = row[1]
            value_range = row[2]
            conversion = row[0]
            
            if seed_value >= base_value and seed_value <= base_value + value_range:
                temp = seed_value - base_value
                seed_value = conversion + temp
                converted = True

    return seed_value



def process_chunk(chunk,almanac):
    results = []

    for i in chunk:
        result = find_location(i,almanac)
        results.append(result)

    return results



def main():
    file_name = "Day-5\\Day5.txt"
    
    # Creating the seed list to read from
    seed_list = {}

    # Handling the first line (seeds)
    first_line = True

    with open(file_name, "r") as file:
        for line in file:
            if first_line:
                rows = [int(x) if x.isdigit() else x for x in line.split()]
                seed_list = rows
                first_line = False
            else:
                rows = [int(x) if x.isdigit() else x for x in line.split()]
                almanac.append(rows)    

    # Call method for finding final seed locations
    pairs = []
    lowest_location = 9999999999999

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []

        for index, seed in enumerate(seed_list):
            if index == 0: continue
            pairs.append(int(seed))
            if (index - 1) % 2:
                total_iterations = pairs[1]

                num_chunks = (total_iterations + chunk_size - 1) // chunk_size

                for chunk_num in range(num_chunks):
                    start = chunk_num * chunk_size + pairs[0]
                    end = min((chunk_num + 1) * chunk_size + pairs[0], pairs[0]+total_iterations)

                    chunk = range(start, end+1)
                    futures.append(executor.submit(process_chunk, chunk, almanac.copy()))


                for future in concurrent.futures.as_completed(futures):
                    results = future.result()
                    for result in results:
                        if lowest_location > result:
                            lowest_location = result

                pairs.clear()

    # Wait for remaining processes to finish
    for future in concurrent.futures.as_completed(futures):
        results = future.result()
        for result in results:
            if lowest_location > result:
                lowest_location = result

    print(lowest_location)

if __name__ == "__main__":
    main()