

# Used ChatGPT to help generate this program.
# Program to count the average number of vowels in a given text file

# List of vowels to count
vowels = "aeiouyAEIOUY"

# Open and read the entire file
with open("pg2701.txt", "r") as file:
    lines = file.readlines()

# Start counting from the line that includes "CHAPTER 1. Loomings."
start_line = "CHAPTER 1. Loomings."
start_index = 0

# Find the starting point in the text
for index, line in enumerate(lines):
    if start_line in line:
        start_index = index
        break

# Process lines starting from the detected index
text = " ".join(lines[start_index:])  # Join all lines after the starting line
words = text.split()  # Split into words

# Count vowels in each word
total_vowel_count = 0
total_word_count = 0

for word in words:
    vowel_count = sum(1 for char in word if char in vowels)
    total_vowel_count += vowel_count
    total_word_count += 1

# Calculate the average number of vowels per word
average_vowels_per_word = total_vowel_count / total_word_count if total_word_count > 0 else 0

# Output the result
print(f"Average number of vowels per word: {average_vowels_per_word:.2f}")

