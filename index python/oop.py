import json
import difflib

# Load JSON data into a Python dictionary
def load_dictionary(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

# Search for a word in the dictionary and return its definition
def get_definition(word, dictionary):
    word = word.lower()  # Convert word to lowercase
    if word in dictionary:
        return dictionary[word]
    else:
        # Check for similar words using difflib
        similar_words = difflib.get_close_matches(word, dictionary.keys(), n=1)
        if similar_words:
            suggestion = similar_words[0]
            yn = input(f"Did you mean '{suggestion}' instead of '{word}'? Enter Y if yes, or N if no: ").lower()
            if yn == 'y':
                return dictionary[suggestion]
            else:
                return "Word not found. Please try again."
        else:
            return "Word not found. Please try again."

# Main function
def main():
    dictionary = load_dictionary(r"C:\plp_projects\index python\data.json")
    
    while True:
        word = input("Enter a word to get its definition (type 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        
        definition = get_definition(word, dictionary)
        print(definition)

if __name__ == "__main__":
    main()
