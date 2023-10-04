#!/usr/bin/env python3

# def print_fibonacci(length):
#     pass


def printFibonacciNumbers(n):

	f1 = 0
	f2 = 1
	if (n < 0):
		return
	print(f1)
 
	for x in range(0, n):
		print(f2,)
		next = f1 + f2
		f1 = f2
		f2 = next


printFibonacciNumbers(8)




