#!/usr/bin/env python3
"""
Math Flash -- The math flashcard game
"""

import random
from datetime import datetime

import humanize


def add(num1, num2):
    '''Add two numbers'''
    return num1 + num2


def sub(num1, num2):
    '''Subtract num2 from num1'''
    return num1 - num2


def mul(num1, num2):
    '''Multiply two numbers'''
    return num1 * num2


def main():
    '''Play a game of math flash cards'''

    operations = {
        'a': {'fcn': add,
              'sym': '+'},
        's': {'fcn': sub,
              'sym': '-'},
        'm': {'fcn': mul,
              'sym': '*'}
    }
    op = input("Would you like (a)ddition, (s)ubtraction, or (m)ultiplication? ").lower()

    if op not in 'asm':
        print("Your choice was not 'a', 's', 'm'.")
        quit(1)

    correct = 0  # Counter for number of correct answers

    start = datetime.now()  # Start time of the quiz

    # Ask 10 questions
    for _ in range(10):
        # Pick 2 random numbers between 1 and 12
        a = random.randint(1, 12)
        b = random.randint(1, 12)

        # Always have 'a' be the bigger number
        if a < b:
            b, a = a, b

        actual = operations[op]['fcn'](a, b)

        answer = input(f"What is {a} {operations[op]['sym']} {b}? ")

        try:
            answer = int(answer)
        except ValueError:
            print("That doesn't look like a number")
            print("")
            continue

        if answer == actual:
            correct = correct + 1
            print("You got it right.  Yay!")
            print("")
        else:
            print(f"The answer was {actual}.  You'll get it next time.")
            print("")

    print(f"You got {correct} out of 10 in {humanize.naturaldelta(datetime.now() - start)}")


if __name__ == "__main__":
    main()
