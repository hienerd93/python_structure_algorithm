#!/bin/python3

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    zenoAmount = 0
    positiveAmount = 0
    for x in arr:
        if x == 0:
            zenoAmount += 1
        if x > 0:
            positiveAmount += 1
    lengArr = len(arr)
    print(positiveAmount/lengArr)
    print((lengArr - positiveAmount - zenoAmount)/lengArr)
    print(zenoAmount/lengArr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
