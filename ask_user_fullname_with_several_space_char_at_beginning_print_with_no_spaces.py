# Ask the user to input their fullname with several space characters at the beginning. 
# Print the input without the spaces in the beginning.

# Ask user's full name 
full_name = input("Enter your full name: ")

# Process text into cleaner version
cleaned_text = full_name.strip() # .strip removes leading and trailing spaces

# Output full name
print(f"Cleaned text: {cleaned_text}")