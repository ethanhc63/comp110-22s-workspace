"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = 730464740

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    quit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character")
    quit()
matching_characters: int = 0
print("Searching for " + character + " in " + word)
if word[0] == character:
    print(character + " found at index 0")
    matching_characters = matching_characters + 1
if word[1] == character:
    print(character + " found at index 1")
    matching_characters = matching_characters + 1
if word[2] == character:
    print(character + " found at index 2")
    matching_characters = matching_characters + 1
if word[3] == character:
    print(character + " found at index 3")
    matching_characters = matching_characters + 1
if word[4] == character:
    print(character + " found at index 4")
    matching_characters = matching_characters + 1
if matching_characters == 0:
    print("No instances of " + character + " found in " + word)
if matching_characters == 1:
    print(str(matching_characters) + " instance of " + character + " found in " + word)
if matching_characters > 1:
    print(str(matching_characters) + " instances of " + character + " found in " + word)