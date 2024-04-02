# File Creation
try:
    # Creating a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Writing at least three lines of text to the file
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Another line with text and numbers: 67890\n")
except PermissionError:
    print("Permission denied. Unable to create or write to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    # Reading the contents of "my_file.txt"
    with open("my_file.txt", "r") as file:
        # Displaying the contents on the console
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("The file 'my_file.txt' was not found.")
except PermissionError:
    print("Permission denied. Unable to read the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File reading process completed.")

# File Appending
try:
    # Opening "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Appending three additional lines of text to the existing content
        file.write("This is an appended line.\n")
        file.write("Appended numbers: 111\n")
        file.write("One more appended line with text: ABC\n")
except FileNotFoundError:
    print("The file 'my_file.txt' was not found.")
except PermissionError:
    print("Permission denied. Unable to append to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending process completed.")
