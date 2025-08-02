"""
Frequency Analysis Program

Analyzes the letter frequency of two user-provided phrases.
Removes all non-letter characters, counts each letter's occurrences,
calculates the percentage of each letter, and displays results
sorted alphabetically and by frequency.
"""

from collections import Counter

# Welcome message
print("Welcome to my Frequency Analysis Program!")

# Define characters to remove from input
non_letter_chars = " .,;:!?'\"()[]{}<>-_=+`~@#$%^&*|\\/\n\t"

# Process first phrase
key_phrase_1 = input("Enter a word or phrase to analyze the frequency of each letter: ")
key_phrase_1 = key_phrase_1.translate(str.maketrans("", "", non_letter_chars)).lower()
letter_count_1 = Counter(key_phrase_1)

# Frequency analysis for first phrase
print(f"\nFrequency analysis for: '{key_phrase_1}'")
print("\nLetter\tOccurrence\tPercentage")
for letter in sorted(letter_count_1):
    count = letter_count_1[letter]
    percentage = (count / len(key_phrase_1)) * 100
    print(f"{letter}\t{count}\t\t{percentage:.2f}%")

# Letters ordered by frequency for first phrase
print("\nLetters ordered by frequency:")
ordered_letters_1 = [letter for letter, _ in letter_count_1.most_common()]
print(", ".join([f"{letter}({count})" for letter, count in letter_count_1.most_common()]))

# Process second phrase
key_phrase_2 = input("\nEnter another word or phrase to analyze the frequency of each letter: ")
key_phrase_2 = key_phrase_2.translate(str.maketrans("", "", non_letter_chars)).lower()
letter_count_2 = Counter(key_phrase_2)

# Frequency analysis for second phrase
print(f"\nFrequency analysis for: '{key_phrase_2}'")
print("\nLetter\tOccurrence\tPercentage")
for letter in sorted(letter_count_2):
    count = letter_count_2[letter]
    percentage = (count / len(key_phrase_2)) * 100
    print(f"{letter}\t{count}\t\t{percentage:.2f}%")

# Letters ordered by frequency for second phrase
print("\nLetters ordered by frequency:")
ordered_letters_2 = [letter for letter, _ in letter_count_2.most_common()]
print(", ".join([f"{letter}({count})" for letter, count in letter_count_2.most_common()]))

# Exit message
print("\nThank you for using my Frequency Analysis Program! Goodbye!")