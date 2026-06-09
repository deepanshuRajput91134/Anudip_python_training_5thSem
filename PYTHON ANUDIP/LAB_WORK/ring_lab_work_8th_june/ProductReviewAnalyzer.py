#Product Review Analyzer
'''_ _ _ __ _. _ _ __ _ _ __ _ _ _ __ _ _ _ __ 
1. Count total words.
2. Create a dictionary containing word frequencies.
3. Find the most frequently used word.
4. Find all words appearing only once.
5. Count words having more than 5 characters.
6. Display words in reverse order.
7. Create a list of unique words.
 _ _ _ _ __ _ _ _ _ _. __ _ _ _ _ '''
 # Product review
review = "This product is excellent excellent excellent and very useful"

# Split review into words
words = review.split()

# Count total words
print("Total Words:", len(words))

# Create dictionary for word frequency
frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

# Display frequencies
print("\nWord Frequencies:")

for word, count in frequency.items():
    print(word, "->", count)

# Find most frequent word
most = max(frequency, key=frequency.get)

print("\nMost Frequent Word:", most)

# Find words appearing once
once = []

for word, count in frequency.items():
    if count == 1:
        once.append(word)

print("Words Appearing Once:")
print(once)

# Count words having more than 5 characters
count = 0

for word in words:
    if len(word) > 5:
        count += 1

print("Words Having More Than 5 Characters:", count)

# Display words in reverse order
reverse_words = words[::-1]

print("Words In Reverse Order:")
print(reverse_words)

# Create list of unique words
unique = list(frequency.keys())

print("Unique Words:")
print(unique)