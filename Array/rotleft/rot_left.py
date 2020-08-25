#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
	result= a[d:] +a[:d]
	ans = " ".join([str(i) for i in result])
	print(ans)

	return ans
if __name__ == '__main__':
	fptr = open('rot_left.txt', 'w')

	nd = input().split()

	n = int(nd[0])

	d = int(nd[1])

	a = list(map(int, input().rstrip().split()))

	import pdb; pdb.set_trace()

	result = rotLeft(a, d)

	fptr.write(' '.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
