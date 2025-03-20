# Ask the user to input their fullname. Print the number of characters in the input.

# Ask user their full name
entered_full_name = input("Enter full name: ")

# Process entered full name by counting characters
character_count = len(entered_full_name) # len() counts characters

# Output counted characters
print(f"There are {character_count} characters.")