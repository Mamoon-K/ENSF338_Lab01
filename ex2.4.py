import timeit

# List of vowels to count
vowels = "aeiouyAEIOUY"

# Open and read the entire file (not included in timing)
with open("pg2701.txt", "r") as file:
    lines = file.readlines()

# Start counting from the line that includes "CHAPTER 1. Loomings."
start_line = "CHAPTER 1. Loomings."
start_index = next((index for index, line in enumerate(lines) if start_line in line), None)

if start_index is None:
    print("Start line not found.")
    exit()

# Process lines starting from the detected index (not included in timing)
text = " ".join(lines[start_index:])  # Join all lines after the starting line
words = text.split()  # Split into words

def compute_average_vowels():
    """Function that performs only the vowel counting."""
    total_vowel_count = 0
    total_word_count = 0

    for word in words:
        vowel_count = sum(1 for char in word if char in vowels)
        total_vowel_count += vowel_count
        total_word_count += 1

    return total_vowel_count / total_word_count if total_word_count > 0 else 0

# Measure execution time over 100 runs
execution_time = timeit.timeit(compute_average_vowels, number=100)

# Compute the final result once (not included in timing)
average_vowels_per_word = compute_average_vowels()

# Output results
print(f"Average number of vowels per word: {average_vowels_per_word:.2f}")
print(f"Average computation time across 100 runs: {execution_time / 100:.6f} seconds")
