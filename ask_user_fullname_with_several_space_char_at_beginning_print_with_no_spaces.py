# ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# ask user's full name 
full_name = input("Enter your full name: ")

# process text into cleaner version
cleaned_text = full_name.strip() # .strip removes leading and trailing spaces

# output fullname
print(f"Cleaned text: {cleaned_text}")