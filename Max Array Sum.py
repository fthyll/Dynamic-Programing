#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return max(arr[0], arr[1])
    
        dp = [0] * len(arr)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
    
        for i in range(2, len(arr)):
            dp[i] = max(arr[i], dp[i-1], arr[i] + dp[i-2])
    
        return dp[-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
