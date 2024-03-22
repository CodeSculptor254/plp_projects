# Accept user input to create a list of integers
numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]  # Convert input strings to integers

# Compute the sum of all integers in the list
sum_of_integers = sum(numbers)
print("Sum of integers:", sum_of_integers)

# Create a tuple containing the names of five favorite books
favorite_books = ("Harry Potter", "It begins with Us", "Twisted Love", "Haunted Adeline", "Ugly Love")

# Use a for loop to print each book name on a separate line
print("My favorite books:")
for book in favorite_books:
    print(book)

# Create an empty dictionary to store person's information
person = {}

# Ask the user for input and store the information in the dictionary
person["name"] = input("Enter your name: ")
person["age"] = input("Enter your age: ")
person["favorite_color"] = input("Enter your favorite_color: ")

# Print results 
print("person's_information")
for key, value in person.items():
    print(key + ":", value)

# Accept user input to create two sets of integers
set1_input = input("Enter integers separated by spaces for the first set: ")
set2_input = input("Enter integers separated by spaces for the second set: ")

# Split the input strings into lists of strings
set1_str_list = set1_input.split()
set2_str_list = set2_input.split()

# Convert the lists of strings into sets of integers
set1 = {int(num_str) for num_str in set1_str_list}
set2 = {int(num_str) for num_str in set2_str_list}

# Find the common element between the two sets
common_element = set1.intersection(set2)

# Print the common elements
print("Common elements:", common_element)

# Store a list of words
words = ["apple", "banana", "grape", "kiwi", "pineapple"]

# Use list comprehension to create a new list with words having odd number of characters
odd_length_words = [word for word in words if len(word) % 2 !=0]

# Print the result
print("Words with odd number of characters:", odd_length_words)