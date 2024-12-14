#ex.1
def count_character_occurrences(input_string, character):
    # Using the count() method to count occurrences of the character
    count = input_string.count(character)
    return count

# Example usage
input_string = "ayush Pandav"
character_to_count = 'a'
result = count_character_occurrences(input_string, character_to_count)
print(f"The character '{character_to_count}' appears {result} times in the string.")

#ex-2
def check_substring_presence():
    input_string = input("Enter the main string: ")
    substring = input("Enter the substring to check: ")
    
    if substring in input_string:
        print(f"The substring '{substring}' is present in the string.")
    else:
        print(f"The substring '{substring}' is not present in the string.")

check_substring_presence()

#ex-3
def split_and_join(input_string, delimiter):
    words = input_string.split()
    
    joined_string = delimiter.join(words)
    
    return joined_string

input_string = "Hello world this is a test"
delimiter = "-"
result = split_and_join(input_string, delimiter)
print(result)  # Output: "Hello-world-this-is-a-test"