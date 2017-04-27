#!/usr/bin/python

# Problem Statement:
# Swap numbers with  out using temp

# Task
# create two variables and assign values and
# swap the values with out using temp variable
# Will use the addition and subtraction property here.

a = 10
b = 5

print("a = %d , b = %d " % (a, b))

a = a + b  # a = 15
b = a - b  # 15 - 5 = 10
a = a - b  # 15 - 10

print("After Swapping ")
print("a = %d , b = %d " % (a, b))
