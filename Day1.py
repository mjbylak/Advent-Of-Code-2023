def sum_calibration_values_from_file(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            # Filter out non-digit characters
            digits = [char for char in line if char.isdigit()]

            # Check if we have at least one digit in the line
            if digits:
                # Combine the first and last digits to form a two-digit number
                value = int(digits[0] + digits[-1])

                # Add the value to the total sum
                total_sum += value

    return total_sum

# Replace 'Day1.txt' with the actual path to your file
file_path = 'Day1.txt'

# Calculate the sum of calibration values from the file
result = sum_calibration_values_from_file(file_path)

# Print the result
print("Sum of calibration values:", result)

