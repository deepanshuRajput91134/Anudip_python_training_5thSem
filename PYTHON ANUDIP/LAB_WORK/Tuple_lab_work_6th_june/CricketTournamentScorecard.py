# Cricket Tournament Scorecard
'''_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
•• Count half-centuries and centuries.
• Find the highest score.
• Display all scores below 20.
• Calculate the average score.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'''
# Cricket Tournament Scorecard

scores = [45, 78, 12, 100, 67, 8, 90, 55]

half_century = 0
century = 0

for score in scores:
    if score >= 50 and score < 100:
        half_century += 1
    elif score >= 100:
        century += 1

print("Half Centuries:", half_century)
print("Centuries:", century)

# Highest score
print("\nHighest Score:", max(scores))

# Scores below 20
print("\nScores below 20:")

for score in scores:
    if score < 20:
        print(score)

# Average score
average = sum(scores) / len(scores)

print("\nAverage Score:", average)