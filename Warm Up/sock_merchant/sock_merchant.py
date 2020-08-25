import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	pair_count=0
	for i in set(ar):
		count = ar.count(i)
		pair_count= pair_count + int(((count - (count % 2))/ 2))

	return pair_count

if __name__ == '__main__':
	fptr = open("sock_merchant_result.txt", 'w')

	n = int(input())

	ar = list(map(int, input().rstrip().split()))

	result = sockMerchant(n, ar)

	fptr.write(str(result) + '\n')

	fptr.close()