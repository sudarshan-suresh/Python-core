#!/usr/bin/python

# Problem Statement :-
# Take 5 subjects marks as an input from the user
# and give grade on the basis of average.

# Task
# 1. Get input for 5 subjects
# 2. find the average and give grade

sub1 = input("Enter mark for sub1: ")
sub2 = input("Enter mark for sub2: ")
sub3 = input("Enter mark for sub3: ")
sub4 = input("Enter mark for sub4: ")
sub5 = input("Enter mark for sub5: ")

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
elif avg >= 70:
    print("C")
elif avg >= 60:
    print("D")
else:
    print("F")
