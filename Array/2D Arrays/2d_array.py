#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
	result = 0 
	for i in range(len(arr)):
		if i <= 3:
			for j in range(len(arr)):
				if j <= 3:
					total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] +	arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
					print('Start point' +str(i) + ' : ' + str(j)  )
					print("Current total "+ str(total))
					print("Current result "+ str(result))

					if total > result:
						result = total
					elif i == 0 and j == 0:
						result = total

	
	print("Final total "+ str(result))
	return result 
    
if __name__ == '__main__':
    fptr = open('2d_array.txt', 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
