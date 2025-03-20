# Ask the user to input a number (0-1000), print the number in 6 digit format. 
# Add zeros at the beginning to complete the 6 digit.

# Ask user to input number (0 - 1000)
entered_number = int(input("Enter number: "))

# Process entered number
formatted_number = str(entered_number).zfill(6) # zfill for formatting int numbers

# Output number as 6 digits
print(f"Formatted number: {formatted_number}")