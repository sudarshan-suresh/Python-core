#!/usr/bin/python
# Problem Statement:
# Calculate Average of numbers from a list.

# Task
# 1. Let the user input the number of elements he want to insert on a list
# and also add elements to the list.
# 2. calculate sum and divide it by the number to get the average

listLength = input("Number of elements need to add in the list : ")
length = int(listLength)
elementList = []
i = 0
while i < length:   # for i in range[0,n]
    val = input("Enter the element: ")
    val = int(val)
    elementList.append(val)
    i += 1
average = sum(elementList) / length

print("Average is %d") % average
