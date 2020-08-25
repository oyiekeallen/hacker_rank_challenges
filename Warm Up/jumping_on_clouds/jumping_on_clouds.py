#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	total_jumps=0
	last_jump = 0
	matches = [i for i, x in enumerate(c) if x == 1]
	for idx, val in enumerate(c) :
		if idx == 0 :
			last_jump = idx
			total_jumps = total_jumps + 1

		if idx > 0  and idx< (len(c) -1 ) :
			if c[idx-1] ==1 or c[idx+1] == 1 :
				last_jump = idx
				total_jumps = total_jumps + 1

			if last_jump + 2 == idx and c[last_jump+1] == 0 and val == 0 and  c[idx+1] != 1  :
				last_jump = idx
				total_jumps = total_jumps + 1	

	return total_jumps

if __name__ == '__main__':
    fptr = open("jumping_on_clouds.txt", 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print("Result :" + str(result))

    fptr.write(str(result) + '\n')

    fptr.close()
