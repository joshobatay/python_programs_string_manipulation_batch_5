# Ask the user to input their fullname in incorrect casing. Print the input in proper casing.

# Ask user their full name
entered_full_name = input('Enter full name: ')

# Process entered full name to proper casing
proper_casing_full_name = entered_full_name.title() # .title converts text to proper casing

# Output full name in proper casing
print(f"Your full name in proper casing: {proper_casing_full_name}")
