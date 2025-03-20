# Ask the user to input a complete statement. Print the number of words in the input

# Ask user complete statement
entered_statement = input("Enter statement here: ")

# Process number of words entered
word_counter = len(entered_statement.split()) # len() counts words, split() splits by spaces

# Output number of words
print(f"There are {word_counter} words.")