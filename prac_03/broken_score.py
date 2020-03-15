"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    # score = float(input("Enter score: "))
    # print(grade_score(score))

    for i in range(1):
        score = random.randint(1, 100)
        print("Your score of {} is {}".format(score, grade_score(score)))


def grade_score(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"


main()
