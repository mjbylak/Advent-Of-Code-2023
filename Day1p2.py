def convert_spelled_digits(word):
    spelled_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    return "".join(spelled_digits.get(char, char) for char in word.lower())

def sum_calibration_values_from_file(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            # Extract all substrings that represent numbers
            numbers = [word for word in line.split() if word.isdigit() or word.isalpha()]

            # Combine the first and last "digits" to form a two-digit number
            for number in numbers:
                converted_number = convert_spelled_digits(number)
                value = int(converted_number[0] + converted_number[-1])
                total_sum += value

    return total_sum

# Replace 'Day1.txt' with the actual path to your file
file_path = 'Day1.txt'

# Calculate the sum of calibration values from the file
result = sum_calibration_values_from_file(file_path)

# Print the result
print("Sum of calibration values:", result)
