#Text Compression Analyzer 
''' __. __ _ _ _ _ _ _. __ _ _ _
1. Count occurrences of each character.
2. Create a dictionary of character frequencies.
3. Display unique characters.
4. Find the most frequent character.
5. Create a compressed output:
A3B3C3D3A3
6. Calculate compression ratio.
_. _ _ _ _ __ _ _ _ _ __ __ __ __ '''
# Original text
text = "AAABBBCCCDDDAAA"

print("Original Text:")
print(text)

# Dictionary for frequencies
frequency = {}

# Count occurrences of characters
for ch in text:

    if ch in frequency:
        frequency[ch] += 1

    else:
        frequency[ch] = 1

# Display character frequencies
print("\nCharacter Frequencies:")

for ch, count in frequency.items():
    print(ch, "->", count)

# Display unique characters
unique = list(frequency.keys())

print("\nUnique Characters:")
print(unique)

# Find most frequent character
most = max(frequency, key=frequency.get)

print("\nMost Frequent Character:", most)

# Create compressed output
compressed = ""

count = 1

for i in range(len(text) - 1):

    if text[i] == text[i + 1]:
        count += 1

    else:
        compressed += text[i] + str(count)
        count = 1

compressed += text[-1] + str(count)

print("\nCompressed Output:")
print(compressed)

# Calculate compression ratio
original_length = len(text)
compressed_length = len(compressed)

ratio = (compressed_length / original_length) * 100

print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", ratio, "%")