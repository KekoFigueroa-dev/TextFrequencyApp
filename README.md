# Frequency Analysis Program

A Python console app that analyzes the letter frequency of any two user-provided phrases.  
It removes all non-letter characters, counts each letter’s occurrences, calculates percentages, and displays results sorted both alphabetically and by frequency.

## Features

- Cleans input to analyze only letters (ignores spaces, punctuation, numbers, etc.)
- Shows how often each letter appears and its percentage in the phrase
- Displays letters ordered from most to least frequent
- Works for two separate phrases in one run

## Usage

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/your-repo-name.git
   ```
2. **Navigate to the project directory:**
   ```
   cd your-repo-name
   ```
3. **Run the program:**
   ```
   python textfrequency.py
   ```

4. **Follow the prompts to enter your phrases and view the analysis.**

## Example Output

```
Welcome to my Frequency Analysis Program!
Enter a word or phrase to analyze the frequency of each letter: Hello, World!
...
Letter   Occurrence   Percentage
d        1            9.09%
e        1            9.09%
h        1            9.09%
l        3           27.27%
o        2           18.18%
r        1            9.09%
w        1            9.09%

Letters ordered by frequency:
lloohwdr
```