import concurrent.futures
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Global Variable Declaration
almanac = []
total_iterations = 0
chunk_size = 1000000
simplify_factor = 1
       
def find_location(seed):
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
                if(seed_value < 120): 
                    print(row)
                    print(seed)
                converted = True

    
    return seed_value



def main():
    file_name = "Day-5/Day5.txt"
    
    # Creating the seed list to read from
    seed_list = {}

    # Handling the first line (seeds)
    first_line = True

    with open(file_name, "r") as file:
        for line in file:
            if first_line:
                rows = [int(x)/simplify_factor if x.isdigit() else x for x in line.split()]
                seed_list = rows
                first_line = False
            else:
                rows = [int(x)/simplify_factor if x.isdigit() else x for x in line.split()]
                almanac.append(rows)    

    # Call method for finding final seed locations
    pairs = []
    lowest_location = 9999999999999
    lower = 1197133308 
    upper = (lower + 38546766) // simplify_factor
    lower //= simplify_factor

    for i in range(lower,upper):
        result = find_location(i)
        if lowest_location > result:
            lowest_location = result
            print(lowest_location)

    for index, seed in enumerate(seed_list):
        if index < 11: continue
        pairs.append(int(seed)//simplify_factor)
        if (index - 1) % 2:
            for i in range(pairs[0],pairs[0]+pairs[1]):
                result = find_location(i)
                if lowest_location > result:
                    lowest_location = result
                    print(lowest_location)

            pairs.clear()



if __name__ == "__main__":
    main()