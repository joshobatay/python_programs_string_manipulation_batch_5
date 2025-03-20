# Ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

# Ask user their full name in incorrect casing
entered_full_name = input("Enter full name: ")

# Process entered full name to reverse casing
reverse_case_full_name = entered_full_name.swapcase() # .swapcase swaps uppercase to lowercase and vice versa

# Output entered full name in reverse case
print(f"Your full name in reverse case: {reverse_case_full_name}")
