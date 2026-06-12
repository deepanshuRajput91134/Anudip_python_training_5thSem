#Library Book Issue Tracker
'''_ _ _. _ _ __ _ _ _ __ _
1. Find the maximum number of issues.
2. Find the minimum number of issues.
3. Calculate the average number of issues.
4. Count books issued more than 15 times.
5. Create a list of books issued fewer than 10 times.
_ _ _ __ _ _. __ _ _ __ _. _ _ _ __ _ _ '''
# Library Book Issue Tracker

book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]


def max_issues(issues):
    return max(issues)


def min_issues(issues):
    return min(issues)


def average_issues(issues):
    return sum(issues) / len(issues)


def count_above_15(issues):
    count = 0

    for issue in issues:
        if issue > 15:
            count += 1

    return count


def issues_below_10(issues):
    low_issues = []

    for issue in issues:
        if issue < 10:
            low_issues.append(issue)

    return low_issues


print("Maximum Issues:", max_issues(book_issues))
print("Minimum Issues:", min_issues(book_issues))
print("Average Issues:", average_issues(book_issues))
print("Books Issued More Than 15 Times:", count_above_15(book_issues))

print("Books Issued Fewer Than 10 Times:")
print(issues_below_10(book_issues))