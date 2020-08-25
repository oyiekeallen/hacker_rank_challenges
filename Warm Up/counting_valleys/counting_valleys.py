#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	level=0
	valley_count=0

	for idx, val in enumerate(s):
		if val.upper() == "U":
			level = level + 1
		elif val.upper() == "D":
			level = level - 1
		
	if idx != 0 and level == 0 and str(s[idx-1]).upper() == "U" :
		print("Previous action: " + str(s[idx-1]).upper())
		print("Level : " + str(level))

		print("Valley countr incremented")
		valley_count = valley_count + 1

		print("Lvl: " + str(level) + " Valleys: " + str(valley_count))
	return valley_count   

    
if __name__ == '__main__':
	fptr = open('counting_valleys_results.txt', 'w')

	n = int(input())

	s = input()

	result = countingValleys(n, s)

	fptr.write(str(result) + '\n')

	fptr.close()
