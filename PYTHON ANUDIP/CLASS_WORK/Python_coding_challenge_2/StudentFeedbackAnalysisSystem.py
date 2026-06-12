# Student Feedback Analysis System

import os

def analyze_feedback():
    try:
        # feedback.txt ka path automatically find karega
        file_path = os.path.join(
            os.path.dirname(__file__),
            "feedback.txt"
        )

        with open(file_path, "r") as file:
            lines = file.readlines()

        # Total Lines
        total_lines = len(lines)

        # Total Words
        total_words = 0
        for line in lines:
            total_words += len(line.split())

        # Total Characters
        total_characters = 0
        for line in lines:
            total_characters += len(line)

        # Longest Feedback
        longest_feedback = max(lines, key=len).strip()

        # Shortest Feedback
        shortest_feedback = min(lines, key=len).strip()

        # Total Vowels
        vowels = "aeiouAEIOU"
        vowel_count = 0

        for line in lines:
            for char in line:
                if char in vowels:
                    vowel_count += 1

        # Output
        print("Total Lines:", total_lines)
        print("Total Words:", total_words)
        print("Total Characters:", total_characters)

        print("\nLongest Feedback:")
        print(longest_feedback)

        print("\nShortest Feedback:")
        print(shortest_feedback)

        print("\nTotal Vowels:", vowel_count)

    except FileNotFoundError:
        print("Error: feedback.txt file not found.")

    except Exception as e:
        print("An error occurred:", e)


# Function Call
analyze_feedback()