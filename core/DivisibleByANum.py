#!/usr/bin/python

# Problem Statement:
# Take lower , upper limit and a number(n)
# print all the numbers in the range divisible by n

# Task
# 1. Get upper ,lower and n from user.
# 2. create range and print numbers which are divisible by n

lower = input("Enter the lower limit: ")
upper = input("Enter the upper limit: ")
n = input("Enter the number for which divisiblity to test ")

for i in range(lower, upper + 1):
    if i % n == 0:
        print(i)
