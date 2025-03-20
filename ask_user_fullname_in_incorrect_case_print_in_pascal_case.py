# Ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# Ask user full name in incorrect casing
entered_full_name = input("Enter full name: ")

# Process full name in incorrect casing to pascal case
full_name_pascal_case = entered_full_name.title().replace(" ", "") # title() for proper casing, replace() for removing spaces

# Output full name to pascal case
