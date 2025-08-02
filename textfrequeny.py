from collections import Counter

# Welcome message
print("Welcome to my the Frequency Analysis Program!")

# Define non-letter characters
non_letter_chars = " .,;:!?'\"()[]{}<>-_=+`~@#$%^&*|\\/\n\t"

# Get and clean user input for key_phrase_1
key_phrase_1 = input("Enter a word or phrase to analyze the frequency of each letter: ")
key_phrase_1 = key_phrase_1.translate(str.maketrans("", "", non_letter_chars)).lower()

# Count letter occurrences and calculate statistics for key_phrase_1
letter_count = Counter(key_phrase_1)
print(letter_count.items())

# Display frequency analysis for key_phrase_1
print(f"Here's the frequency analysis for '{key_phrase_1}':")
print("\n\tLetter\tOccurrence\tPercentage")
for key,value in letter_count.items():
    percentage = (value / len(key_phrase_1)) * 100
    print(f"\t{key.upper()}\t{value}\t\t{percentage:.2f}%")

# Display letters ordered by frequency for key_phrase_1
print("\nLetters ordered by frequency:")
for letter, freq in letter_count.most_common():
    print(f"{letter.upper()}: {freq}")

# Get and clean user input for key_phrase_2
key_phrase_2 = input("Enter another word or phrase to analyze the frequency of each letter: ")
key_phrase_2 = key_phrase_2.translate(str.maketrans("", "", non_letter_chars)).lower()

# Repeat process for key_phrase_2
letter_count = Counter(key_phrase_2)
print(letter_count.items())

# Display frequency analysis and ordered letters for key_phrase_2
print(f"Here's the frequency analysis for '{key_phrase_2}':")
print("\n\tLetter\tOccurrence\tPercentage") 
for key,value in letter_count.items():
    percentage = (value / len(key_phrase_2)) * 100
    print(f"\t{key.upper()}\t{value}\t\t{percentage:.2f}%")

print("\nLetters ordered by frequency:")
for letter, freq in letter_count.most_common():
    print(f"{letter.upper()}: {freq}")

# Print goodbye message
print("\nThank you for using my Frequency Analysis Program! Goodbye!")