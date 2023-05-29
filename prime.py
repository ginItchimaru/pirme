#!/usr/bin/env python3

import math
import sys


def is_prime(x):

	if x < 2:

		return False

	elif x == 2:

		return True

	elif x % 2 == 0:

		return False

	else:

		for i in range(3, int(math.sqrt(x)) + 1, 2):

			if x % i == 0:

				return False

		return True



def input_prime():

	if len(sys.argv) != 2:

		print("Usage: primeNumber.py number")
		sys.exit(1)

	try:

		input = int(sys.argv[1])

	except ValueError:

		print("Input must be a valid number")
		sys.exit(1)


	if is_prime(input) == True:

		print(f"\n{input} is a prime number\n")

	else:

		print(f"\n{input} is not a prime number\n")





if __name__ == '__main__':
	input_prime()