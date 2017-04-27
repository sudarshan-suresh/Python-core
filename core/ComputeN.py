#!/usr/bin/python

# Problem Statement :
# Get user input n and add n + nn + nnn

# Task
# 1. get user input
# 2. multiply by 2 and  3 on string and add the int values.

n = input("Enter a number : ")
strN = str(n)
nn = strN * 2
nnn = strN * 3
sum1 = int(n) + int(nn) + int(nnn)
print("n+nn+nnn is = %d ", sum1)
