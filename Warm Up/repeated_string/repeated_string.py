#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
	if len(s) == 1:
		return n
	else :
		reminder = n % len(s)
		multiplier = int(n / len(s) )
		return (s.count('a') * multiplier) + s[:reminder].count('a')
if __name__ == '__main__':
    fptr = open(("repeated_string.txt", 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
