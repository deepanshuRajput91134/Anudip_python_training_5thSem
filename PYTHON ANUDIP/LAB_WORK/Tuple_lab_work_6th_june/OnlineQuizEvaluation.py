#Online Quiz Evaluation
'''_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ 
• Calculate score.
• Display incorrectly answered question numbers.
• Count correct and wrong answers.
• Determine pass/fail (minimum 60%).
_ _ _ _ _ _ _ _ _ _ _ _'''
# Online Quiz Evaluation

correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

score = 0
wrong_questions = []

for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
    else:
        wrong_questions.append(i + 1)

print("Score:", score)

print("\nIncorrect Question Numbers:")
print(wrong_questions)

# Correct and wrong count
correct_count = score
wrong_count = len(correct) - score

print("\nCorrect Answers:", correct_count)
print("Wrong Answers:", wrong_count)

# Pass/Fail
percentage = (score / len(correct)) * 100

if percentage >= 60:
    print("\nPass")
else:
    print("\nFail")