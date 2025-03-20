# ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# ask user's fullname 
full_name = input("Enter your full name: ")

# process text into cleaner version
cleaned_full_name = full_name.strip() # .strip removes leading and trailing spaces

# output fullname
