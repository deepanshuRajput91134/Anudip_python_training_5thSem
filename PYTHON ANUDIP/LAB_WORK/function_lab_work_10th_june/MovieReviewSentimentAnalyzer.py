#  #Movie Review Sentiment Analyzer
# '''_ _. _ __ __ _ _ _ _ _ __ _ _ __ 
# Create the following functions:
# 1. count_sentiments(reviews)
# Counts:
# • Excellent
# • Good
# • Average
# • Poor reviews
# 2. most_common_word(reviews)
# Returns the most frequently occurring word.
# 3. longest_review(reviews)
# Returns the review containing the maximum number of characters.
# 4. reviews_with_keyword(reviews, keyword)
# Displays all reviews containing a given keyword.
# _. __ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _'''
reviews = [
"excellent movie",
"average story",
"excellent acting",
"poor direction",
"excellent visuals",
"poor screenplay",
"good music",
"excellent climax",
"average performance",
"good cinematography"
]

# 1. Count sentiments
def count_sentiments(reviews):
    excellent = good = average = poor = 0

    for r in reviews:
        if "excellent" in r:
            excellent += 1
        elif "good" in r:
            good += 1
        elif "average" in r:
            average += 1
        elif "poor" in r:
            poor += 1

    print("Excellent Reviews:", excellent)
    print("Good Reviews:", good)
    print("Average Reviews:", average)
    print("Poor Reviews:", poor)

# 2. Most common word
def most_common_word(reviews):
    words = []

    for r in reviews:
        words.extend(r.split())

    return max(set(words), key=words.count)

# 3. Longest review
def longest_review(reviews):
    return max(reviews, key=len)

# 4. Reviews with keyword
def reviews_with_keyword(reviews, keyword):
    for r in reviews:
        if keyword in r:
            print(r)


# Function calls
count_sentiments(reviews)

print("\nMost Common Word:")
print(most_common_word(reviews))

print("\nLongest Review:")
print(longest_review(reviews))

print("\nReviews containing 'excellent':")
reviews_with_keyword(reviews, "excellent")
