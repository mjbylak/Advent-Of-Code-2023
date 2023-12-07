from pprint import pprint

# Debugging
debug_parse = False
debug_num_cards = False
debug_scores = False

# Global Variables
card_list = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

def find_type(hand):
    num_values = [0] * 14

    potential_output = 1
    got_pair = False

    for index, value in enumerate(card_list):
        num_values[index] = hand.count(value)

    if debug_num_cards: pprint(num_values)

    for i in range(14):
        if num_values[i] == 5: potential_output = 7 #fivekind
        elif num_values[i] == 4: potential_output = 6 #fourkind
        elif num_values[i] == 3 and got_pair: potential_output = 5 #fullhouse
        elif num_values[i] == 3: potential_output = 4 #threekind
        elif num_values[i] == 2 and got_pair: potential_output = 3 #twopair
        elif num_values[i] == 2: 
            got_pair = True
            potential_output = 2 #pair
    return potential_output


def collect_hand(input):
    hands = []
    for hand in input:
        hands.append(find_type(hand[0]))
    return hands


def main():
    file_name = "Day-7\\Day7Cal.txt"
    
    input = []


    global rows

    with open(file_name, "r") as file:
        for line in file:
            input.append(line.split())

    if debug_parse: pprint(input) 
    
    if debug_scores: pprint(collect_hand(input))




if __name__ == "__main__":
    main()