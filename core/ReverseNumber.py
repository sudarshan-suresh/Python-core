#!/usr/bin/python

# Problem Statement :-
# Reverse a number

# Task
# 1. get the input from user.
# reverse the number using the / and % operator.

n = input("Enter a number: ")
print(n)
rev = ""
rev1 = 0
while n > 0:
    remainder = n % 10
    n = n/10
    rev += str(remainder)
    rev1 = rev1 * 10 + remainder

print("reverse is %d " % (rev1))
