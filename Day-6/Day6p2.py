from pprint import pprint

debug_parse = False
debug_cropping = False
debug_pairing = False
debug_distance = False
debug_comparison = False
debug_each_win = False

def find_distance(time, charge):
    # if debug_distance: print(f"After charging {charge}, traveled {(time-charge)*charge}")
    return (time-charge) * charge



def find_wins(time,distance):
    if debug_pairing: print(f"time is {time} record is {distance}")

    wins = 0

    for i in range(time):
        travel = find_distance(time, i)
        if debug_comparison: print(f"We found that the boat travelled {travel} versus the record of {distance}")
        if travel > distance:
            wins += 1

    if debug_each_win: print(f"We've found {wins} from the {time} and {distance}")

    return wins



def find_all_wins(input):
    product_wins = 1
    for i in range(len(input[0])):
        wins = find_wins(input[0][i],input[1][i])
        if  wins > 0:
            product_wins *= wins

    return product_wins



def main():
    file_name = "Day-6\\Day6Cal.txt"
    
    input = []

    global rows

    with open(file_name, "r") as file:
        for line in file:
            rows = [int(x) if x.isdigit() else x for x in line.split()]
            # Append empty lists for each row
            input.append(rows)


            if debug_parse: pprint(rows)

    if debug_parse: pprint(input)

    for i in range(2):
        input[i] = input[i][1:len(input[i])]
    
    if debug_cropping: pprint(input)

    new_input = ["",""]
    for i in range(len(input)):
        print(f"i is {i}")
        for j in range(len(input[0])):
            print(f"    j is {j}")
            new_input[i] += str((input[i][j]))

    lazy = [[int(new_input[0])],[int(new_input[1])]]

    pprint(lazy)

    print(find_all_wins(lazy))



if __name__ == "__main__":
    main()