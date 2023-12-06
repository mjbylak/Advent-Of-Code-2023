from pprint import pprint

debug_parse = False
debug_check_winner = False

def check_winner(left, right):
    wins = 0
    points = 0
    if debug_check_winner: 
        pprint(left)
        pprint(right)
    for pulls in left:
        for winners in right:
            if pulls == winners: 
                wins += 1
                if debug_check_winner: print(f"Matched {pulls} with {winners}")
    if(wins > 0):
        points = 2**(wins-1)
    if debug_check_winner: print(points)
    return points

def main():
    file_name = "Day-4\\Day4.txt"
    
    input = [[],[]]

# Array of this:
# "Card 1:" array of numbers, split at | array of numbers
    past_colon = False
    with open(file_name, "r") as file:
        for index, line in enumerate(file):
            rows = [int(x) if x.isdigit() else x for x in line.split()]
            if debug_parse: pprint(rows)
            # Append empty lists for each row
            input[0].append([])
            input[1].append([])

            input[0][index], input[1][index] = rows[2:rows.index("|")],rows[rows.index("|")+1:len(rows)]
            if debug_parse: pprint(rows)

    if debug_parse: pprint(input)

    points = 0

    for i in range(len(input[0])):
        points += check_winner(input[0][i],input[1][i])

    print(points)


if __name__ == "__main__":
    main()