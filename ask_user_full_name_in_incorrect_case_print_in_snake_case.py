# Ask the user to input their fullname in incorrect casing. Print the input in snake case.

# Ask user their full name in incorrect casing
entered_full_name = input("Enter your full name: ")

# Process entered full name in incorrect casing to snake case
snake_case_full_name = entered_full_name.lower().replace(" ", "_")

# Output entered full name to snake case
print(f"Your full name in snake case: {snake_case_full_name} ")
